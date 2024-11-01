document.getElementById("scenarioForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
    const prompt = document.getElementById("prompt").value;

    // Fetch the generated scenario from the backend
    fetch(`http://127.0.0.1:5000/generate_scenario?prompt=${encodeURIComponent(prompt)}`)
        .then(response => response.json())
        .then(data => {
            // Display the result
            const resultDiv = document.getElementById("result");
            if (data.status === "success") {
                resultDiv.innerHTML = `<h2>Generated Scenario:</h2><pre>${data.scenario}</pre>`;
            } else {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        })
        .catch(error => {
            console.error("Error:", error);
            const resultDiv = document.getElementById("result");
            resultDiv.innerHTML = "<p>An error occurred while generating the scenario.</p>";
        });
});
