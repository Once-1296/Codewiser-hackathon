export default function TaskInput({ taskInput, handleTaskChange, addTask }) {
  const isFormValid = taskInput.title.trim() !== "";

  return (
    <div className="glass-card animate-slide-up delay-2" style={{ padding: "24px", borderRadius: "12px", marginBottom: "24px" }}>
      <h3 style={{ marginTop: 0, marginBottom: "20px" }}>2. Add Tasks</h3>

      <div style={{ marginBottom: "15px" }}>
        <label style={{ display: "block", marginBottom: "8px", fontSize: "14px" }}>Task Title</label>
        <input
          name="title"
          placeholder="e.g., Review Linked Lists"
          value={taskInput.title}
          onChange={handleTaskChange}
          className="modern-input"
        />
      </div>

      <div style={{ display: "flex", gap: "15px", marginBottom: "20px" }}>
        <div style={{ flex: 1 }}>
          <label style={{ display: "block", marginBottom: "8px", fontSize: "14px" }}>Time (mins)</label>
          <input
            type="number"
            name="estimated_time"
            value={taskInput.estimated_time}
            onChange={handleTaskChange}
            className="modern-input"
          />
        </div>
        
        <div style={{ flex: 1 }}>
          <label style={{ display: "block", marginBottom: "8px", fontSize: "14px" }}>Subject</label>
          <select
            name="subject"
            value={taskInput.subject}
            onChange={handleTaskChange}
            className="modern-input"
          >
            <option value="dsa">DSA</option>
            <option value="math">Math</option>
            <option value="physics">Physics</option>
            <option value="english">English</option>
            <option value="history">History</option>
          </select>
        </div>
      </div>

      <button
        onClick={addTask}
        disabled={!isFormValid}
        className={`btn-primary ${isFormValid ? "active" : ""}`}
        style={{ padding: "12px" }}
      >
        + Add Task
      </button>
    </div>
  );
}