export default function UserForm({ userState, handleUserChange }) {
  
  // Internal helper to prevent typing numbers outside range
  const handleSafeChange = (e) => {
    const { name, value, min, max } = e.target;
    let val = parseInt(value);

    // If it's a number input and has a value, clamp it
    if (e.target.type === "number" && value !== "") {
      if (min && val < parseInt(min)) val = parseInt(min);
      if (max && val > parseInt(max)) val = parseInt(max);
      
      // Create a fake event object to pass to the parent handler
      handleUserChange({
        target: {
          name: name,
          value: val
        }
      });
    } else {
      handleUserChange(e);
    }
  };

  return (
    <div 
      className="glass-card animate-fade-in delay-1" 
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
          01.
        </span> 
        Your State
      </h2>

      <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
        <div style={{ flex: "1 1 200px" }}>
          <label className="modern-label">Sleep Hours (0-16)</label>
          <input
            type="number"
            name="sleep_hours"
            placeholder="e.g., 7"
            min="0"
            max="16"
            step="0.25"
            value={userState.sleep_hours}
            onChange={handleSafeChange}
            className="modern-input"
            style={{ backgroundColor: "#1a1a1a" }} // Force dark background
          />
          <div style={{ fontSize: "0.85rem", color: "#9ca3af", marginTop: "6px" }}>
            Enter hours between 0.0 and 16.0
          </div>
        </div>

        <div style={{ flex: "1 1 200px" }}>
          <label className="modern-label">Stress Level (1-5)</label>
          <input
            type="number"
            name="stress_level"
            min="1"
            max="5"
            step="1"
            placeholder="e.g., 3"
            value={userState.stress_level}
            onChange={handleSafeChange}
            className="modern-input"
            style={{ backgroundColor: "#1a1a1a" }} // Force dark background
          />
          <div style={{ fontSize: "0.85rem", color: "#9ca3af", marginTop: "6px" }}>
            Integer between 1 (low) and 5 (high)
          </div>
        </div>
      </div>

      <div>
        <label className="modern-label">Preferred Time of Day</label>
        <select
          name="time_of_day"
          value={userState.time_of_day}
          onChange={handleUserChange}
          className="modern-input"
          style={{ 
            cursor: "pointer", 
            backgroundColor: "#1a1a1a", 
            color: "white" 
          }}
        >
          <option value="morning">Morning (6 AM - 12 PM)</option>
          <option value="afternoon">Afternoon (12 PM - 5 PM)</option>
          <option value="evening">Evening (5 PM - 9 PM)</option>
          <option value="night">Night (9 PM - 2 AM)</option>
        </select>
      </div>
    </div>
  );
}