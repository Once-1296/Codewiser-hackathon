export default function Loader() {
  return (
    <div
      className="glass-card animate-slide-up"
      style={{
        textAlign: "center",
        padding: "40px 20px",
        borderRadius: "12px",
        marginTop: "30px",
        border: "1px solid var(--accent-border)",
      }}
    >
      <div className="loader-spinner"></div>
      <h3 style={{ color: "var(--accent)", margin: "0 0 10px 0", fontSize: "20px" }}>
        Optimizing Schedule...
      </h3>
      <p style={{ fontSize: "14px", margin: 0, opacity: 0.8 }}>
        Please wait while our models evaluate energy patterns to build your ideal plan.
      </p>
    </div>
  );
}