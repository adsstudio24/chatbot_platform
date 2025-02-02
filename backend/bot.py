from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "your-api-key-here"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Користувач: {data['message']}",
        max_tokens=100
    )
    return jsonify({"reply": response["choices"][0]["text"].strip()})

if __name__ == '__main__':
    app.run(debug=True)
