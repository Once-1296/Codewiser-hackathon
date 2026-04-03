export default function TaskList({ tasks, deleteTask }) {
  // Empty State UI
  if (tasks.length === 0) {
    return (
      <div 
        className="glass-card animate-fade-in delay-3" 
        style={{ padding: "32px", textAlign: "center" }}
      >
        <div className="empty-state-dash">
          <div style={{ fontSize: "2rem", marginBottom: "12px" }}>📋</div>
          <h3 style={{ margin: "0 0 8px 0", color: "var(--text-heading)" }}>
            Your Queue is Empty
          </h3>
          <p style={{ margin: 0, fontSize: "0.9rem", color: "var(--text-muted)" }}>
            Add tasks above to start building your optimized study plan.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div 
      className="glass-card animate-fade-in delay-3" 
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
          03.
        </span> 
        Task Queue
      </h2>
      
      <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
        {tasks.map((t, i) => (
          <div
            key={i}
            className="animate-fade-in"
            style={{
              background: "rgba(0, 0, 0, 0.2)",
              border: "1px solid rgba(255, 255, 255, 0.05)",
              borderRadius: "12px",
              padding: "16px 20px",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              borderLeft: "4px solid var(--accent-primary)",
              animationDelay: `${i * 0.1}s`,
              transition: "transform 0.2s ease, background 0.2s ease"
            }}
            onMouseOver={(e) => e.currentTarget.style.background = "rgba(0, 0, 0, 0.4)"}
            onMouseOut={(e) => e.currentTarget.style.background = "rgba(0, 0, 0, 0.2)"}
          >
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: "12px", marginBottom: "10px" }}>
                <strong style={{ 
                  color: "var(--text-heading)", 
                  fontSize: "1.1rem", 
                  letterSpacing: "0.02em" 
                }}>
                  {t.title}
                </strong>

                {/* show difficulty/classification if available */}
                {t.difficulty && (
                  <span style={{
                    fontSize: "0.7rem",
                    fontWeight: 700,
                    color: "white",
                    background: t.difficulty === 'hard' ? '#ef4444' : t.difficulty === 'medium' ? '#f59e0b' : '#34d399',
                    padding: '6px 8px',
                    borderRadius: '8px',
                    textTransform: 'uppercase'
                  }}>
                    {String(t.difficulty).toUpperCase()}
                  </span>
                )}
              </div>
              
              <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
                <span style={{ 
                  fontSize: "0.75rem", 
                  fontWeight: "600",
                  background: "rgba(255,255,255,0.08)", 
                  color: "var(--text-main)",
                  padding: "6px 12px", 
                  borderRadius: "20px",
                  letterSpacing: "0.05em"
                }}>
                  ⏱ {t.estimated_time} MINS
                </span>
                
                <span style={{ 
                  fontSize: "0.75rem", 
                  fontWeight: "600",
                  background: "var(--accent-glow)", 
                  color: "var(--text-heading)",
                  padding: "6px 12px", 
                  borderRadius: "20px",
                  textTransform: "uppercase",
                  letterSpacing: "0.05em"
                }}>
                  📚 {t.subject}
                </span>
              </div>
            </div>

            <button
              onClick={() => deleteTask(i)}
              style={{
                background: "var(--danger-bg)",
                border: "1px solid rgba(239, 68, 68, 0.3)",
                width: "36px",
                height: "36px",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                borderRadius: "50%",
                cursor: "pointer",
                color: "var(--danger)",
                fontSize: "1rem",
                transition: "all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
                flexShrink: 0,
                marginLeft: "16px"
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.background = "var(--danger)";
                e.currentTarget.style.color = "white";
                e.currentTarget.style.transform = "rotate(90deg) scale(1.1)";
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.background = "var(--danger-bg)";
                e.currentTarget.style.color = "var(--danger)";
                e.currentTarget.style.transform = "rotate(0deg) scale(1)";
              }}
              aria-label="Delete Task"
            >
              ✕
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}