export default function Loader() {
  return (
    <div
      className="glass-card animate-fade-in"
      style={{
        textAlign: "center",
        padding: "48px 24px",
        marginTop: "16px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center"
      }}
    >
      <div className="loader-wrapper">
        <div className="loader-circle"></div>
        <div className="loader-inner"></div>
      </div>
      
      <h3 style={{ 
        color: "var(--text-heading)", 
        margin: "16px 0 8px 0", 
        fontSize: "1.25rem",
        letterSpacing: "0.02em"
      }}>
        Optimizing Your Workflow...
      </h3>
      
      <p style={{ 
        color: "var(--text-muted)", 
        fontSize: "0.95rem", 
        margin: 0, 
        maxWidth: "400px",
        lineHeight: "1.6"
      }}>
        Please wait while our models evaluate your energy patterns and task requirements to build your perfect plan.
      </p>
    </div>
  );
}