export default function TaskList({ tasks, deleteTask }) {
  if (tasks.length === 0) return null;

  return (
    <div className="animate-slide-up delay-3" style={{ marginBottom: "24px" }}>
      <h3 style={{ marginTop: 0, marginBottom: "15px" }}>3. Task List</h3>
      
      {tasks.map((t, i) => (
        <div
          key={i}
          className="glass-card animate-slide-up"
          style={{
            padding: "16px",
            borderRadius: "10px",
            marginBottom: "12px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderLeft: "4px solid var(--accent)",
            animationDelay: `${i * 0.1}s`
          }}
        >
          <div>
            <strong style={{ color: "white", display: "block", marginBottom: "8px", fontSize: "16px" }}>
              {t.title}
            </strong>
            <div style={{ display: "flex", gap: "8px" }}>
              <span style={{ 
                fontSize: "12px", 
                background: "rgba(255,255,255,0.05)", 
                padding: "4px 10px", 
                borderRadius: "20px" 
              }}>
                ⏱ {t.estimated_time} mins
              </span>
              <span style={{ 
                fontSize: "12px", 
                background: "rgba(192, 132, 252, 0.1)", 
                color: "var(--accent)",
                padding: "4px 10px", 
                borderRadius: "20px",
                textTransform: "capitalize"
              }}>
                📚 {t.subject}
              </span>
            </div>
          </div>

          <button
            onClick={() => deleteTask(i)}
            style={{
              background: "rgba(255, 77, 77, 0.1)",
              border: "1px solid rgba(255, 77, 77, 0.3)",
              padding: "8px 12px",
              borderRadius: "8px",
              cursor: "pointer",
              color: "#ff4d4d",
              transition: "all 0.2s"
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.background = "#ff4d4d";
              e.currentTarget.style.color = "white";
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.background = "rgba(255, 77, 77, 0.1)";
              e.currentTarget.style.color = "#ff4d4d";
            }}
          >
            ✕
          </button>
        </div>
      ))}
    </div>
  );
}