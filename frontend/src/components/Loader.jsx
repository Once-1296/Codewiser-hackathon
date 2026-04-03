export default function Loader() {
  return (
    <div
      style={{
        textAlign: "center",
        padding: "30px 20px",
        background: "#2a2a2a",
        borderRadius: "8px",
        marginTop: "20px",
        border: "1px dashed #4CAF50",
      }}
    >
      <h3 style={{ color: "#4CAF50", margin: "0 0 10px 0", fontSize: "20px" }}>
        Generating Schedule... ⏳
      </h3>
      <p style={{ color: "#bbb", fontSize: "14px", margin: 0 }}>
        Please wait while our ML models analyze your energy levels and optimize your tasks.
      </p>
    </div>
  );
}