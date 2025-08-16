# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from tarotai.core import tarotAI_functions

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    spread_id = data.get('spreadID', 0)
    result = tarotAI_functions.tell(spreadID=spread_id)

    spread_str = str(result)  # result — це Spread обʼєкт
    ai_result = ""

    return jsonify({
        'spread': spread_str,
        'ai': ai_result
    })

@app.route('/ai', methods=['POST'])
def ai():
    data = request.get_json()
    spread_text = data.get('spreadText')
    if not spread_text:
        return jsonify({'ai': 'No spread text provided.'}), 400

    ai_result = tarotAI_functions.askAI(spread_text)  # твоя функція AI-інтерпретації
    return jsonify({'ai': ai_result})

if __name__ == '__main__':
    app.run(debug=True)
