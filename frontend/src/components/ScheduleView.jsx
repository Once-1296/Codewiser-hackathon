export default function ScheduleView({ schedule }) {
  if (!schedule || schedule.length === 0) return null;

  const isArray = Array.isArray(schedule);

  const handlePrint = () => {
    window.print();
  };

  const getEfficiencyColor = (efficiency) => {
    if (efficiency >= 0.8) return "var(--success)"; // Green
    if (efficiency >= 0.5) return "var(--warning)"; // Orange
    return "var(--danger)"; // Red
  };

  // Robust parser to handle if backend sends 0.8, 80, or "80%"
  const parseEfficiency = (rawEff) => {
    if (rawEff == null) return 0;
    let val = typeof rawEff === 'string' ? parseFloat(rawEff.replace('%', '')) : rawEff;
    if (isNaN(val)) return 0;
    return val > 1 ? val / 100 : val; // Convert 80 to 0.8
  };

  return (
    <div 
      className="glass-card animate-fade-in delay-1" 
      style={{ 
        padding: "32px", 
        display: "flex", 
        flexDirection: "column", 
        gap: "24px",
        marginTop: "16px",
        position: "relative",
        overflow: "hidden"
      }}
    >
      {/* Decorative Background Glow */}
      <div style={{
        position: "absolute",
        top: "-50px",
        right: "-50px",
        width: "150px",
        height: "150px",
        background: "var(--accent-glow)",
        filter: "blur(60px)",
        zIndex: 0,
        pointerEvents: "none"
      }}></div>

      <div style={{ 
        display: "flex", 
        justifyContent: "space-between", 
        alignItems: "center",
        borderBottom: "1px solid var(--glass-border)", 
        paddingBottom: "16px",
        zIndex: 1
      }}>
        <h2 style={{ fontSize: "1.5rem", margin: 0, display: "flex", alignItems: "center" }}>
          <span style={{ color: "var(--accent-primary)", marginRight: "12px", fontSize: "1.2rem" }}>
            04.
          </span> 
          Your Optimized Plan
        </h2>

        <button 
          onClick={handlePrint}
          style={{
            background: "rgba(255,255,255,0.05)",
            border: "1px solid rgba(255,255,255,0.1)",
            color: "var(--text-main)",
            padding: "8px 16px",
            borderRadius: "8px",
            cursor: "pointer",
            fontSize: "0.85rem",
            fontWeight: "600",
            transition: "all 0.2s ease"
          }}
          onMouseOver={(e) => {
            e.currentTarget.style.background = "rgba(255,255,255,0.1)";
            e.currentTarget.style.borderColor = "var(--accent-primary)";
          }}
          onMouseOut={(e) => {
            e.currentTarget.style.background = "rgba(255,255,255,0.05)";
            e.currentTarget.style.borderColor = "rgba(255,255,255,0.1)";
          }}
        >
          🖨 Save PDF
        </button>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "16px", zIndex: 1 }}>
        {isArray ? (
          <div style={{ 
            borderLeft: "2px solid rgba(255,255,255,0.1)", 
            marginLeft: "10px", 
            paddingLeft: "24px", 
            display: "flex", 
            flexDirection: "column", 
            gap: "20px" 
          }}>
            {schedule.map((item, index) => {
              // Robust extractions
              const title = item.task || item.title || item.name || "Study Block";
              const timeSlot = item.time_slot ?? (item.start_time && item.end_time ? `${item.start_time} - ${item.end_time}` : item.time || "");
              const duration = item.duration ? `${item.duration} mins` : "";
              const isBreak = title.toLowerCase().includes("break");
              
              // Efficiency parsing
              const efficiency = parseEfficiency(item.expected_efficiency ?? item.efficiency);
              const efColor = getEfficiencyColor(efficiency);

              return (
                <div 
                  key={`${timeSlot}-${title}-${index}`} 
                  className="animate-fade-in"
                  style={{ 
                    position: "relative",
                    animationDelay: `${index * 0.1}s` 
                  }}
                >
                  {/* Timeline Dot colored by efficiency (or green if break) */}
                  <div style={{
                    position: "absolute",
                    left: "-31px",
                    top: "50%",
                    transform: "translateY(-50%)",
                    width: "12px",
                    height: "12px",
                    borderRadius: "50%",
                    background: isBreak ? "var(--success)" : efColor,
                    boxShadow: `0 0 10px ${isBreak ? "var(--success)" : efColor}`
                  }}></div>

                  <div style={{
                    background: isBreak ? "rgba(16, 185, 129, 0.05)" : "rgba(0,0,0,0.2)",
                    border: `1px solid ${isBreak ? "rgba(16, 185, 129, 0.2)" : "rgba(255,255,255,0.05)"}`,
                    borderLeft: !isBreak ? `4px solid ${efColor}` : "4px solid var(--success)",
                    borderRadius: "12px",
                    padding: "16px 20px",
                    transition: "transform 0.2s ease"
                  }}
                  onMouseOver={(e) => e.currentTarget.style.transform = "translateX(5px)"}
                  onMouseOut={(e) => e.currentTarget.style.transform = "translateX(0)"}
                  >
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", flexWrap: "wrap", gap: "10px" }}>
                      
                      {/* Left Side: Task Info */}
                      <div>
                        <strong style={{ 
                          display: "block", 
                          color: isBreak ? "var(--success)" : "var(--text-heading)", 
                          fontSize: "1.1rem", 
                          marginBottom: "8px" 
                        }}>
                          {title}
                        </strong>
                        <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
                          {timeSlot && (
                            <span style={{ fontSize: "0.8rem", background: "rgba(0,0,0,0.4)", padding: "4px 10px", borderRadius: "6px" }}>
                              🕒 {timeSlot}
                            </span>
                          )}
                          {duration && (
                            <span style={{ fontSize: "0.8rem", background: "rgba(0,0,0,0.4)", padding: "4px 10px", borderRadius: "6px" }}>
                              ⏱ {duration}
                            </span>
                          )}
                        </div>
                      </div>
                      
                      {/* Right Side: Efficiency Badge */}
                      {!isBreak && efficiency > 0 && (
                        <div style={{
                          fontSize: "0.75rem",
                          color: efColor,
                          fontWeight: "bold",
                          background: "rgba(0,0,0,0.4)",
                          border: `1px solid ${efColor}`,
                          padding: "6px 12px",
                          borderRadius: "8px",
                          letterSpacing: "0.05em"
                        }}>
                          ⚡ EFFICIENCY: {(efficiency * 100).toFixed(0)}%
                        </div>
                      )}

                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div style={{
            background: "rgba(0,0,0,0.2)",
            border: "1px solid rgba(255,255,255,0.05)",
            borderRadius: "12px",
            padding: "24px",
            whiteSpace: "pre-wrap",
            lineHeight: "1.7",
            color: "var(--text-main)",
            fontFamily: "var(--sans)",
            fontSize: "0.95rem"
          }}>
            {schedule}
          </div>
        )}
      </div>
    </div>
  );
}