import { useState } from "react";

function App() {

  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);

  const generate = async () => {

    const response = await fetch(
      "http://localhost:8000/generate",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
      }
    );

    const data = await response.json();

    setResult(data);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>AI App Compiler</h1>

      <textarea
        rows={12}
        cols={100}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br /><br />

      <button onClick={generate}>
        Generate
      </button>

      <pre>
        {JSON.stringify(result, null, 2)}
      </pre>
    </div>
  );
}

export default App;