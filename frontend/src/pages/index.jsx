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
    if (!taskInput.title) return;
    setTasks([...tasks, taskInput]);
    setTaskInput({ title: "", estimated_time: 30, subject: "dsa" });
  };

  const deleteTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  const handleGenerate = async () => {
    if (tasks.length === 0) {
      alert("Please add at least one task!");
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

  const isGenerateDisabled = isLoading || tasks.length === 0;

  return (
    <div
      className="animate-slide-up"
      style={{
        padding: "40px 20px",
        maxWidth: "650px",
        margin: "0 auto",
      }}
    >
      <h1 style={{ 
        textAlign: "center", 
        fontSize: "42px", 
        marginBottom: "40px",
        background: "linear-gradient(to right, #c084fc, #8b5cf6)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent"
      }}>
        Study Planner
      </h1>

      <UserForm userState={userState} handleUserChange={handleUserChange} />
      <TaskInput taskInput={taskInput} handleTaskChange={handleTaskChange} addTask={addTask} />
      <TaskList tasks={tasks} deleteTask={deleteTask} />

      <hr style={{ borderColor: "rgba(255,255,255,0.05)", margin: "30px 0" }} />

      <button
        onClick={handleGenerate}
        disabled={isGenerateDisabled}
        className={`btn-primary ${!isGenerateDisabled ? "active" : ""}`}
        style={{ animation: !isGenerateDisabled && !isLoading ? "pulse 2s infinite" : "none" }}
      >
        {isLoading ? "Generating Schedule... ⏳" : "Generate Optimized Schedule"}
      </button>

      {isLoading && <Loader />}
      {!isLoading && schedule && <ScheduleView schedule={schedule} />}
    </div>
  );
}