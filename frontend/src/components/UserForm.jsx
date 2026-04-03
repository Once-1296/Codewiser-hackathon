export default function UserForm({ userState, handleUserChange }) {
  return (
    <div style={{
      background: "#2a2a2a",
      padding: "20px",
      borderRadius: "8px",
      marginBottom: "20px"
    }}>
      <h3 style={{ marginTop: 0, marginBottom: "15px", color: "#f3f4f6" }}>1. Your State</h3>

      <div style={{ marginBottom: "12px" }}>
        <label style={{ display: "block", marginBottom: "5px", fontSize: "14px", color: "#bbb" }}>
          Sleep Hours
        </label>
        <input
          type="number"
          name="sleep_hours"
          placeholder="e.g., 7"
          value={userState.sleep_hours}
          onChange={handleUserChange}
          style={{ 
            width: "100%", 
            padding: "10px", 
            borderRadius: "6px", 
            border: "1px solid #444", 
            background: "#1e1e1e", 
            color: "white",
            boxSizing: "border-box"
          }}
        />
      </div>

      <div style={{ marginBottom: "12px" }}>
        <label style={{ display: "block", marginBottom: "5px", fontSize: "14px", color: "#bbb" }}>
          Stress Level (1-5)
        </label>
        <input
          type="number"
          name="stress_level"
          min="1"
          max="5"
          placeholder="e.g., 3"
          value={userState.stress_level}
          onChange={handleUserChange}
          style={{ 
            width: "100%", 
            padding: "10px", 
            borderRadius: "6px", 
            border: "1px solid #444", 
            background: "#1e1e1e", 
            color: "white",
            boxSizing: "border-box"
          }}
        />
      </div>

      <div>
        <label style={{ display: "block", marginBottom: "5px", fontSize: "14px", color: "#bbb" }}>
          Preferred Time of Day
        </label>
        <select
          name="time_of_day"
          value={userState.time_of_day}
          onChange={handleUserChange}
          style={{ 
            width: "100%", 
            padding: "10px", 
            borderRadius: "6px", 
            border: "1px solid #444", 
            background: "#1e1e1e", 
            color: "white",
            boxSizing: "border-box"
          }}
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