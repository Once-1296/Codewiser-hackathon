export default function ScheduleView({ schedule }) {
  if (!schedule || schedule.length === 0) return null;

  // Helper to visually highlight efficiency levels
  const getEfficiencyColor = (efficiency) => {
    if (efficiency >= 0.8) return "#4CAF50"; // Green for high efficiency
    if (efficiency >= 0.5) return "#ff9800"; // Orange for medium
    return "#f44336"; // Red for low
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h2 style={{ textAlign: "center", color: "#c084fc", marginBottom: "20px" }}>
        Your Optimized Schedule
      </h2>
      
      <div style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
        {schedule.map((item, i) => (
          <div
            key={i}
            style={{
              padding: "16px",
              background: "#2a2a2a",
              borderRadius: "10px",
              borderLeft: `5px solid ${getEfficiencyColor(item.efficiency)}`,
              boxShadow: "0 4px 6px rgba(0,0,0,0.1)",
              display: "flex",
              flexDirection: "column",
              gap: "12px"
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              {/* Readable Time Block */}
              <div style={{
                background: "#1e1e1e",
                padding: "6px 12px",
                borderRadius: "6px",
                color: "#c084fc",
                fontWeight: "bold",
                fontSize: "14px",
                letterSpacing: "0.5px"
              }}>
                ⏰ {item.start_time} - {item.end_time}
              </div>

              {/* Efficiency Highlight */}
              <div style={{
                fontSize: "13px",
                color: getEfficiencyColor(item.efficiency),
                fontWeight: "bold",
                background: "#1e1e1e",
                padding: "4px 8px",
                borderRadius: "4px"
              }}>
                Efficiency: {(item.efficiency * 100).toFixed(0)}%
              </div>
            </div>

            {/* Task Title */}
            <div style={{ fontSize: "18px", color: "white", fontWeight: "500" }}>
              {item.task}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}