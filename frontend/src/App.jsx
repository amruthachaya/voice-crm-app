import { useState } from "react";

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

function App() {
  const [transcript, setTranscript] = useState("");
  const [listening, setListening] = useState(false);
  const [extracted, setExtracted] = useState(null);
  const [evals, setEvals] = useState([]);

  const startRecording = () => {
    if (!SpeechRecognition) {
      alert("Speech Recognition not supported");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-IN";
    recognition.continuous = false;

    recognition.onstart = () => setListening(true);

    recognition.onresult = (event) => {
      setTranscript(event.results[0][0].transcript);
    };

    recognition.onend = () => setListening(false);

    recognition.start();
  };

  const sendToBackend = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/extract/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ transcript }),
    });
    const data = await res.json();
    setExtracted(data);
  };

  const loadEvals = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/evals/");
    const data = await res.json();
    setEvals(data);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>🎤 Voice CRM Logger</h2>

      <button onClick={startRecording}>
        {listening ? "Listening..." : "Start Recording"}
      </button>

      <h4>Transcript</h4>
      <textarea
        rows="3"
        style={{ width: "100%" }}
        value={transcript}
        onChange={(e) => setTranscript(e.target.value)}
      />

      <br />
      <button onClick={sendToBackend} disabled={!transcript}>
        Extract Data
      </button>

      {extracted && (
        <>
          <h3>📦 Extracted JSON</h3>
          <pre>{JSON.stringify(extracted, null, 2)}</pre>
        </>
      )}

      <hr />

      <h3>📊 Evaluation Dashboard</h3>
      <button onClick={loadEvals}>Run Evaluations</button>

      {evals.length > 0 && (
        <table border="1" cellPadding="5" style={{ marginTop: "10px" }}>
          <thead>
            <tr>
              <th>Test ID</th>
              <th>Expected Name</th>
              <th>Actual Name</th>
              <th>Expected Phone</th>
              <th>Actual Phone</th>
              <th>HITL Verified</th>
            </tr>
          </thead>
          <tbody>
            {evals.map((row, idx) => (
              <tr key={idx}>
                <td>{row.test_id}</td>
                <td>{row.expected_name}</td>
                <td>{row.actual_name}</td>
                <td>{row.expected_phone}</td>
                <td>{row.actual_phone}</td>
                <td>{row.hitl_verified ? "Yes" : "No"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
