export default function TaskInput({ taskInput, handleTaskChange, addTask }) {
  const isFormValid = taskInput.title.trim() !== "";

  return (
    <div style={{
      background: "#2a2a2a",
      padding: "20px",
      borderRadius: "8px",
      marginBottom: "20px"
    }}>
      <h3 style={{ marginTop: 0, marginBottom: "15px", color: "#f3f4f6" }}>2. Add Tasks</h3>

      <div style={{ marginBottom: "12px" }}>
        <label style={{ display: "block", marginBottom: "5px", fontSize: "14px", color: "#bbb" }}>
          Task Title
        </label>
        <input
          name="title"
          placeholder="e.g., Review Linked Lists"
          value={taskInput.title}
          onChange={handleTaskChange}
          style={{ 
            width: "100%", 
            padding: "10px", 
            borderRadius: "6px", 
            border: "1px solid #444", 
            background: "#1e1e1e", 
            color: "white",
            boxSizing: "border-box"
          }}
        />
      </div>

      <div style={{ display: "flex", gap: "10px", marginBottom: "15px" }}>
        <div style={{ flex: 1 }}>
          <label style={{ display: "block", marginBottom: "5px", fontSize: "14px", color: "#bbb" }}>
            Time (mins)
          </label>
          <input
            type="number"
            name="estimated_time"
            value={taskInput.estimated_time}
            onChange={handleTaskChange}
            style={{ 
              width: "100%", 
              padding: "10px", 
              borderRadius: "6px", 
              border: "1px solid #444", 
              background: "#1e1e1e", 
              color: "white",
              boxSizing: "border-box"
            }}
          />
        </div>
        
        <div style={{ flex: 1 }}>
          <label style={{ display: "block", marginBottom: "5px", fontSize: "14px", color: "#bbb" }}>
            Subject
          </label>
          <select
            name="subject"
            value={taskInput.subject}
            onChange={handleTaskChange}
            style={{ 
              width: "100%", 
              padding: "10px", 
              borderRadius: "6px", 
              border: "1px solid #444", 
              background: "#1e1e1e", 
              color: "white",
              boxSizing: "border-box"
            }}
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
        style={{
          padding: "12px",
          width: "100%",
          background: isFormValid ? "#aa3bff" : "#555",
          color: isFormValid ? "white" : "#999",
          border: "none",
          borderRadius: "6px",
          cursor: isFormValid ? "pointer" : "not-allowed",
          fontWeight: "bold",
          transition: "background 0.3s"
        }}
      >
        + Add Task
      </button>
    </div>
  );
}