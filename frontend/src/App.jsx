import { useState } from "react";
import { generateSchedule } from "./services/api";

function App() {
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

  // -------------------------
  // User State
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

  // -------------------------
  // Task Input
  // -------------------------
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

  // -------------------------
  // Generate Schedule
  // -------------------------
  const handleGenerate = async () => {
    try {
      const res = await generateSchedule({
        user_state: userState,
        tasks: tasks,
      });

      setSchedule(res.data.schedule);
    } catch (err) {
      console.error(err);
      alert("Error generating schedule");
    }
  };

  // -------------------------
  // UI
  // -------------------------
  return (
    <div
      style={{
        padding: "20px",
        maxWidth: "600px",
        margin: "40px auto",
        background: "#1e1e1e",
        borderRadius: "10px",
        color: "white",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Study Planner</h1>

      {/* USER STATE */}
      <h3 style={{ marginTop: "20px" }}>User State</h3>

      <input
        type="number"
        name="sleep_hours"
        placeholder="Sleep Hours"
        value={userState.sleep_hours}
        onChange={handleUserChange}
        style={{ marginBottom: "10px", width: "100%", padding: "8px" }}
      />

      <input
        type="number"
        name="stress_level"
        placeholder="Stress (1-5)"
        value={userState.stress_level}
        onChange={handleUserChange}
        style={{ marginBottom: "10px", width: "100%", padding: "8px" }}
      />

      <select
        name="time_of_day"
        value={userState.time_of_day}
        onChange={handleUserChange}
        style={{ marginBottom: "10px", width: "100%", padding: "8px" }}
      >
        <option value="morning">Morning</option>
        <option value="afternoon">Afternoon</option>
        <option value="evening">Evening</option>
        <option value="night">Night</option>
      </select>

      <hr />

      {/* TASK INPUT */}
      <h3 style={{ marginTop: "20px" }}>Add Task</h3>

      <input
        name="title"
        placeholder="Task title"
        value={taskInput.title}
        onChange={handleTaskChange}
        style={{ marginBottom: "10px", width: "100%", padding: "8px" }}
      />

      <input
        type="number"
        name="estimated_time"
        value={taskInput.estimated_time}
        onChange={handleTaskChange}
        style={{ marginBottom: "10px", width: "100%", padding: "8px" }}
      />

      <select
        name="subject"
        value={taskInput.subject}
        onChange={handleTaskChange}
        style={{ marginBottom: "10px", width: "100%", padding: "8px" }}
      >
        <option value="dsa">DSA</option>
        <option value="math">Math</option>
        <option value="physics">Physics</option>
        <option value="english">English</option>
        <option value="history">History</option>
      </select>

      <button
        onClick={addTask}
        style={{
          marginTop: "10px",
          padding: "10px",
          width: "100%",
          cursor: "pointer",
        }}
      >
        Add Task
      </button>

      {/* TASK LIST */}
      <h3 style={{ marginTop: "20px" }}>Tasks</h3>

      {tasks.map((t, i) => (
        <div
          key={i}
          style={{
            padding: "12px",
            background: "#2a2a2a",
            borderRadius: "8px",
            marginBottom: "10px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div>
            <strong>{t.title}</strong>
            <br />
            <span style={{ fontSize: "12px", color: "#bbb" }}>
              {t.estimated_time} mins • {t.subject}
            </span>
          </div>

          <button
            onClick={() => deleteTask(i)}
            style={{
              background: "#ff4d4d",
              border: "none",
              padding: "6px 10px",
              borderRadius: "5px",
              cursor: "pointer",
              color: "white",
            }}
          >
            ✕
          </button>
        </div>
      ))}

      <hr />

      {/* GENERATE */}
      <button
        onClick={handleGenerate}
        style={{
          marginTop: "10px",
          padding: "12px",
          width: "100%",
          background: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "6px",
          cursor: "pointer",
        }}
      >
        Generate Schedule
      </button>

      {/* OUTPUT */}
      {schedule && (
        <div style={{ marginTop: "20px" }}>
          <h3>Schedule</h3>

          {schedule.map((item, i) => (
            <div
              key={i}
              style={{
                padding: "10px",
                background: "#333",
                borderRadius: "6px",
                marginBottom: "10px",
              }}
            >
              <strong>{item.task}</strong>
              <br />
              Time: {item.start_time} - {item.end_time}
              <br />
              Efficiency: {item.efficiency?.toFixed(2)}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;