export default function TaskInput({ taskInput, handleTaskChange, addTask, remainingMinutes }) {
  const titleValid = taskInput.title && taskInput.title.trim() !== "";
  const timeValid = Number.isInteger(Number(taskInput.estimated_time)) && Number(taskInput.estimated_time) >= 5 && Number(taskInput.estimated_time) <= 300;
  const fitsRemaining = Number(taskInput.estimated_time) <= remainingMinutes;
  const isFormValid = titleValid && timeValid && fitsRemaining;

  return (
    <div 
      className="glass-card animate-fade-in delay-2" 
      style={{ 
        padding: "32px", 
        display: "flex", 
        flexDirection: "column", 
        gap: "24px" 
      }}
    >
      <h2 style={{ 
        fontSize: "1.5rem", 
        borderBottom: "1px solid var(--glass-border)", 
        paddingBottom: "16px", 
        margin: 0,
        display: "flex",
        alignItems: "center"
      }}>
        <span style={{ color: "var(--accent-primary)", marginRight: "12px", fontSize: "1.2rem" }}>
          02.
        </span> 
        Add Tasks
      </h2>

      <div>
        <label className="modern-label">Task Title</label>
        <input
          name="title"
          placeholder="e.g., Master Linked Lists, Read Chapter 4"
          value={taskInput.title}
          onChange={handleTaskChange}
          className="modern-input"
        />
      </div>

      <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
        <div style={{ flex: "1 1 200px" }}>
          <label className="modern-label">Time (mins)</label>
          <input
            type="number"
            name="estimated_time"
            min="5"
            step="5"
            value={taskInput.estimated_time}
            onChange={handleTaskChange}
            className="modern-input"
          />
          <div style={{ marginTop: "6px", fontSize: "0.85rem", color: remainingMinutes <= 60 ? "#ffb86b" : "#9ca3af" }}>
            {remainingMinutes <= 0 ? (
              "No remaining minutes available (max total 720 mins)."
            ) : (
              `Remaining allocatable minutes: ${remainingMinutes}`
            )}
          </div>
        </div>
        
        <div style={{ flex: "1 1 200px" }}>
          <label className="modern-label">Subject</label>
          <select
            name="subject"
            value={taskInput.subject}
            onChange={handleTaskChange}
            className="modern-input"
            style={{ cursor: "pointer" }}
          >
            <option value="dsa">Data Structures & Algorithms</option>
            <option value="math">Mathematics</option>
            <option value="physics">Physics</option>
            <option value="english">English Literature</option>
            <option value="history">History</option>
          </select>
        </div>
      </div>

      <button
        onClick={addTask}
        disabled={!isFormValid}
        className={`btn-primary ${isFormValid ? "active" : ""}`}
        style={{ marginTop: "8px" }}
        title={!titleValid ? "Provide a task title" : !timeValid ? "Time must be 5-300 mins" : !fitsRemaining ? "Exceeds remaining minutes" : "Add task"}
      >
        + Add Task to Queue
      </button>
    </div>
  );
}