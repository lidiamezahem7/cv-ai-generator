import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("https://cv-ai-generator-1.onrender.com/optimize", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data.optimized);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Générateur de CV IA</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <button onClick={handleSubmit}>Optimiser</button>

      <textarea value={result} rows={20} style={{ width: "100%" }} />
    </div>
  );
}

export default App;
