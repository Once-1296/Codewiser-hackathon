import { useState } from "react";
import { generateSchedule } from "../services/api";

import UserForm from "../components/UserForm";
import TaskInput from "../components/TaskInput";
import TaskList from "../components/TaskList";
import ScheduleView from "../components/ScheduleView";
import Loader from "../components/Loader";

export default function IndexPage() {
  const [userState, setUserState] = useState({
    sleep_hours: 7,
    stress_level: 3,
    time_of_day: "morning",
  });

  const [taskInput, setTaskInput] = useState({
    title: "",
    estimated_time: 30,
    subject: "dsa",
  });

  const [tasks, setTasks] = useState([]);
  const [schedule, setSchedule] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isShaking, setIsShaking] = useState(false);

  const handleUserChange = (e) => {
    setUserState({
      ...userState,
      [e.target.name]:
        e.target.name === "sleep_hours" || e.target.name === "stress_level"
          ? Number(e.target.value)
          : e.target.value,
    });
  };

  const handleTaskChange = (e) => {
    setTaskInput({
      ...taskInput,
      [e.target.name]:
        e.target.name === "estimated_time"
          ? Number(e.target.value)
          : e.target.value,
    });
  };

  const addTask = () => {
    if (!taskInput.title.trim()) return;
    setTasks([...tasks, taskInput]);
    setTaskInput({ title: "", estimated_time: 30, subject: "dsa" });
  };

  const deleteTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  const triggerShake = () => {
    setIsShaking(true);
    setTimeout(() => setIsShaking(false), 400);
  };

  const handleGenerate = async () => {
    if (tasks.length === 0) {
      triggerShake();
      return;
    }

    setIsLoading(true);
    setSchedule(null);

    try {
      const res = await generateSchedule({
        user_state: userState,
        tasks: tasks,
      });
      setSchedule(res.data.schedule);
    } catch (err) {
      console.error(err);
      alert("Error generating schedule. Make sure backend is running.");
    } finally {
      setIsLoading(false);
    }
  };

  const isGenerateDisabled = isLoading;
  const hasTasks = tasks.length > 0;

  return (
    <div
      className="animate-fade-in"
      style={{
        padding: "60px 20px",
        maxWidth: "768px",
        margin: "0 auto",
        display: "flex",
        flexDirection: "column",
        gap: "24px"
      }}
    >
      <div style={{ textAlign: "center", marginBottom: "20px" }}>
        <h1 className="gradient-text" style={{ fontSize: "3.5rem", marginBottom: "8px" }}>
          Study Planner
        </h1>
        <p style={{ color: "var(--text-muted)", fontSize: "1.1rem", maxWidth: "500px", margin: "0 auto" }}>
          Optimize your learning workflow with AI-driven schedule generation.
        </p>
      </div>

      <UserForm userState={userState} handleUserChange={handleUserChange} />
      
      <TaskInput taskInput={taskInput} handleTaskChange={handleTaskChange} addTask={addTask} />
      
      <TaskList tasks={tasks} deleteTask={deleteTask} />

      <div style={{ margin: "20px 0" }}>
        <button
          onClick={handleGenerate}
          disabled={isGenerateDisabled}
          className={`
            btn-primary delay-4 animate-fade-in 
            ${hasTasks && !isLoading ? "active" : ""} 
            ${isShaking ? "animate-shake" : ""}
          `}
          style={{ 
            animation: hasTasks && !isLoading 
              ? "fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards, pulseGlow 2.5s infinite" 
              : "fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards",
            padding: "20px",
            fontSize: "1.15rem"
          }}
        >
          {isLoading ? "Analyzing Patterns... ⏳" : "Generate Optimized Schedule ✨"}
        </button>
      </div>

      {isLoading && <Loader />}
      {!isLoading && schedule && <ScheduleView schedule={schedule} />}
    </div>
  );
}