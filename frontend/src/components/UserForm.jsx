export default function UserForm({ userState, handleUserChange }) {
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
          <label className="modern-label">Sleep Hours</label>
          <input
            type="number"
            name="sleep_hours"
            placeholder="e.g., 7"
            value={userState.sleep_hours}
            onChange={handleUserChange}
            className="modern-input"
          />
        </div>

        <div style={{ flex: "1 1 200px" }}>
          <label className="modern-label">Stress Level (1-5)</label>
          <input
            type="number"
            name="stress_level"
            min="1"
            max="5"
            placeholder="e.g., 3"
            value={userState.stress_level}
            onChange={handleUserChange}
            className="modern-input"
          />
        </div>
      </div>

      <div>
        <label className="modern-label">Preferred Time of Day</label>
        <select
          name="time_of_day"
          value={userState.time_of_day}
          onChange={handleUserChange}
          className="modern-input"
          style={{ cursor: "pointer" }}
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