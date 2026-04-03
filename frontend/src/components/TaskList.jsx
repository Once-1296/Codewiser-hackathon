export default function TaskList({ tasks, deleteTask }) {
  if (tasks.length === 0) {
    return null; // Return nothing if there are no tasks yet
  }

  return (
    <div style={{ marginBottom: "20px" }}>
      <h3 style={{ marginTop: 0, marginBottom: "15px", color: "#f3f4f6" }}>3. Task List</h3>
      
      {tasks.map((t, i) => (
        <div
          key={i}
          style={{
            padding: "12px 16px",
            background: "#2a2a2a",
            borderRadius: "8px",
            marginBottom: "10px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderLeft: "4px solid #aa3bff"
          }}
        >
          <div>
            <strong style={{ color: "white", display: "block", marginBottom: "6px", fontSize: "16px" }}>
              {t.title}
            </strong>
            <div>
              <span style={{ 
                fontSize: "12px", 
                color: "#bbb", 
                background: "#1e1e1e", 
                padding: "3px 8px", 
                borderRadius: "4px", 
                marginRight: "8px" 
              }}>
                ⏱ {t.estimated_time} mins
              </span>
              <span style={{ 
                fontSize: "12px", 
                color: "#bbb", 
                background: "#1e1e1e", 
                padding: "3px 8px", 
                borderRadius: "4px",
                textTransform: "capitalize"
              }}>
                📚 {t.subject}
              </span>
            </div>
          </div>

          <button
            onClick={() => deleteTask(i)}
            style={{
              background: "transparent",
              border: "1px solid #ff4d4d",
              padding: "6px 12px",
              borderRadius: "5px",
              cursor: "pointer",
              color: "#ff4d4d",
              fontWeight: "bold",
            }}
          >
            ✕
          </button>
        </div>
      ))}
    </div>
  );
}