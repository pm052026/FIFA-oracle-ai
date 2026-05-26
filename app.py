from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Create Gemini client
client = genai.Client(api_key="ENTER_YOUR_API_KEY_HERE")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        team1 = data["team1"]
        team2 = data["team2"]

        prompt = f"""
        Predict the football match between {team1} and {team2}.

        Give:
        1. Winning probability
        2. Predicted score
        3. Key players
        4. Tactical analysis
        5. Final winner prediction
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return jsonify({
            "result": response.text
        })

    except Exception as e:
        return jsonify({
            "result": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)