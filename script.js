async function predictMatch() {

    const team1 = document.getElementById("team1").value;
    const team2 = document.getElementById("team2").value;

    const resultBox = document.getElementById("result");

    resultBox.innerHTML = `
    <div class="loading">
        ⚽ AI is predicting the match...
    </div>
    `;

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            team1: team1,
            team2: team2
        })
    });

    const data = await response.json();

    resultBox.innerText = data.result;
}