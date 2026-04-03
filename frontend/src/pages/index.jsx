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
  const [isLoading, setIsLoading] = useState(false); // NEW: Loading state

  // -------------------------
  // Handlers
  // -------------------------
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

    setIsLoading(true); // Disable button & show loader
    setSchedule(null);  // Clear previous schedule while loading

    try {
      const res = await generateSchedule({
        user_state: userState,
        tasks: tasks,
      });
      // console.log(res.data.schedule)
      setSchedule(res.data.schedule);
    } catch (err) {
      console.error(err);
      alert("Error generating schedule. Make sure backend is running.");
    } finally {
      setIsLoading(false); // Re-enable button & hide loader
    }
  };

  // -------------------------
  // UI
  // -------------------------
  const isGenerateDisabled = isLoading || tasks.length === 0;

  return (
    <div
      style={{
        padding: "20px",
        maxWidth: "600px",
        margin: "40px auto",
        background: "#1e1e1e",
        borderRadius: "10px",
        color: "white",
        fontFamily: "system-ui, 'Segoe UI', Roboto, sans-serif",
      }}
    >
      <h1 style={{ textAlign: "center", color: "#f3f4f6", fontSize: "32px", margin: "10px 0 30px" }}>
        Study Planner
      </h1>

      <UserForm userState={userState} handleUserChange={handleUserChange} />
      
      <TaskInput taskInput={taskInput} handleTaskChange={handleTaskChange} addTask={addTask} />
      
      <TaskList tasks={tasks} deleteTask={deleteTask} />

      <hr style={{ borderColor: "#333", margin: "20px 0" }} />

      <button
        onClick={handleGenerate}
        disabled={isGenerateDisabled}
        style={{
          padding: "14px",
          width: "100%",
          background: isGenerateDisabled ? "#555" : "#4CAF50",
          color: isGenerateDisabled ? "#999" : "white",
          border: "none",
          borderRadius: "6px",
          cursor: isGenerateDisabled ? "not-allowed" : "pointer",
          fontSize: "16px",
          fontWeight: "bold",
          transition: "background 0.3s"
        }}
      >
        {isLoading ? "Generating... ⏳" : "Generate Schedule"}
      </button>

      {/* Conditional Rendering for Loading and Result */}
      {isLoading && <Loader />}
      {!isLoading && schedule && <ScheduleView schedule={schedule} />}
      
    </div>
  );
}