export default function ScheduleView({ schedule }) {
  if (!schedule || schedule.length === 0) return null;

  const isArray = Array.isArray(schedule);

  const handlePrint = () => {
    window.print();
  };

  const getEfficiencyColor = (efficiency) => {
    // Using Hex codes ensures the CSS linear-gradient and box-shadow work perfectly
    if (efficiency >= 0.8) return "#10b981"; // Success Green
    if (efficiency >= 0.5) return "#f59e0b"; // Warning Orange
    return "#ef4444"; // Danger Red
  };

  const parseEfficiency = (rawEff) => {
    if (rawEff == null) return 0;
    let val = typeof rawEff === 'string' ? parseFloat(rawEff.replace('%', '')) : rawEff;
    if (isNaN(val)) return 0;
    return val > 1 ? val / 100 : val;
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
              const title = item.task || item.title || item.name || "Study Block";
              const timeSlot = item.time_slot ?? (item.start_time && item.end_time ? `${item.start_time} - ${item.end_time}` : item.time || "");
              const isBreak = title.toLowerCase().includes("break");
              
              const efficiency = parseEfficiency(item.expected_efficiency ?? item.efficiency);
              const efColor = getEfficiencyColor(efficiency);

              return (
                <div 
                  key={`${timeSlot}-${title}-${index}`} 
                  className="animate-fade-in"
                  style={{ position: "relative", animationDelay: `${index * 0.1}s` }}
                >
                  <div style={{
                    position: "absolute",
                    left: "-31px",
                    top: "50%",
                    transform: "translateY(-50%)",
                    width: "12px",
                    height: "12px",
                    borderRadius: "50%",
                    background: isBreak ? "#10b981" : efColor,
                    boxShadow: `0 0 10px ${isBreak ? "#10b981" : efColor}`,
                    zIndex: 2
                  }}></div>

                  <div style={{
                    background: "rgba(0,0,0,0.2)",
                    border: "1px solid rgba(255,255,255,0.05)",
                    borderLeft: `4px solid ${isBreak ? "#10b981" : efColor}`,
                    borderRadius: "12px",
                    padding: "20px",
                    transition: "transform 0.2s ease"
                  }}>
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "8px" }}>
                              <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
                                <strong style={{ color: "var(--text-heading)", fontSize: "1.1rem" }}>
                                  {title}
                                </strong>

                                {/* Difficulty badge (if present) */}
                                {(() => {
                                  const diff = item.difficulty ?? item.classification ?? null;
                                  if (!diff) return null;
                                  const diffLabel = String(diff).toUpperCase();
                                  const colors = { easy: "#34d399", medium: "#f59e0b", hard: "#ef4444" };
                                  const bg = colors[String(diff).toLowerCase()] || "#9ca3af";
                                  return (
                                    <span style={{
                                      fontSize: "0.7rem",
                                      fontWeight: 700,
                                      color: "white",
                                      background: bg,
                                      padding: "6px 8px",
                                      borderRadius: "8px",
                                      letterSpacing: "0.03em"
                                    }}>
                                      {diffLabel}
                                    </span>
                                  );
                                })()}

                                <span style={{ fontSize: "0.85rem", opacity: 0.8, fontWeight: "600", marginLeft: "auto" }}>
                                  🕒 {timeSlot}
                                </span>
                              </div>
                    </div>

                    {!isBreak && (
                      <div style={{ marginTop: "12px" }}>
                        <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.7rem", marginBottom: "4px", color: efColor, fontWeight: "bold", textTransform: "uppercase" }}>
                          <span>Focus Efficiency</span>
                          <span>{(efficiency * 100).toFixed(0)}%</span>
                        </div>
                        <div className="energy-bar-container">
                          <div 
                            className="energy-bar-fill" 
                            style={{ 
                              width: `${efficiency * 100}%`, 
                              backgroundColor: efColor, /* Fallback */
                              background: `linear-gradient(90deg, ${efColor}aa, ${efColor})`,
                              boxShadow: `0 0 12px ${efColor}66`
                            }} 
                          />
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div className="glass-card" style={{ padding: "20px", whiteSpace: "pre-wrap" }}>
            {schedule}
          </div>
        )}
      </div>
    </div>
  );
}