export default function TaskInput({ taskInput, handleTaskChange, addTask }) {
  const isFormValid = taskInput.title.trim() !== "";

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
      >
        + Add Task to Queue
      </button>
    </div>
  );
}