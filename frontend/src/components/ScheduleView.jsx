export default function ScheduleView({ schedule }) {
  if (!schedule || schedule.length === 0) return null;

  const getEfficiencyColor = (efficiency) => {
    if (efficiency >= 0.8) return "#4ade80"; 
    if (efficiency >= 0.5) return "#fb923c"; 
    return "#f87171"; 
  };

  return (
    <div style={{ marginTop: "40px" }} className="animate-slide-up">
      <h2 style={{ textAlign: "center", color: "white", marginBottom: "30px", fontSize: "28px" }}>
        Your Optimized Schedule
      </h2>
      
      <div style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
        {schedule.map((item, i) => {
          const timeSlot = item.time_slot ?? (item.start_time && item.end_time ? `${item.start_time} - ${item.end_time}` : "");
          const efficiency = item.expected_efficiency ?? item.efficiency ?? 0;
          const efColor = getEfficiencyColor(efficiency);

          return (
            <div
              key={`${timeSlot}-${item.task}-${i}`}
              className="glass-card animate-slide-up"
              style={{
                padding: "20px",
                borderRadius: "12px",
                borderLeft: `5px solid ${efColor}`,
                display: "flex",
                flexDirection: "column",
                gap: "14px",
                animationDelay: `${i * 0.15}s`
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <div style={{
                  background: "rgba(0,0,0,0.3)",
                  padding: "6px 14px",
                  borderRadius: "8px",
                  color: "white",
                  fontWeight: "bold",
                  fontSize: "14px",
                  letterSpacing: "0.5px"
                }}>
                  ⏰ {timeSlot}
                </div>

                <div style={{
                  fontSize: "13px",
                  color: efColor,
                  fontWeight: "bold",
                  background: "rgba(0,0,0,0.3)",
                  padding: "4px 10px",
                  borderRadius: "6px"
                }}>
                  Efficiency: {(efficiency * 100).toFixed(0)}%
                </div>
              </div>

              <div style={{ fontSize: "18px", color: "white", fontWeight: "500" }}>
                {item.task}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}