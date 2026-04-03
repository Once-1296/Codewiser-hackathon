export default function UserForm({ userState, handleUserChange }) {
  return (
    <div className="glass-card animate-slide-up delay-1" style={{ padding: "24px", borderRadius: "12px", marginBottom: "24px" }}>
      <h3 style={{ marginTop: 0, marginBottom: "20px" }}>1. Your State</h3>

      <div style={{ marginBottom: "15px" }}>
        <label style={{ display: "block", marginBottom: "8px", fontSize: "14px" }}>Sleep Hours</label>
        <input
          type="number"
          name="sleep_hours"
          placeholder="e.g., 7"
          value={userState.sleep_hours}
          onChange={handleUserChange}
          className="modern-input"
        />
      </div>

      <div style={{ marginBottom: "15px" }}>
        <label style={{ display: "block", marginBottom: "8px", fontSize: "14px" }}>Stress Level (1-5)</label>
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

      <div>
        <label style={{ display: "block", marginBottom: "8px", fontSize: "14px" }}>Preferred Time of Day</label>
        <select
          name="time_of_day"
          value={userState.time_of_day}
          onChange={handleUserChange}
          className="modern-input"
        >
          <option value="morning">Morning</option>
          <option value="afternoon">Afternoon</option>
          <option value="evening">Evening</option>
          <option value="night">Night</option>
        </select>
      </div>
    </div>
  );
}