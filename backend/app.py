from flask import Flask, request, jsonify
from ai_agent import handle_call
from supervisor_handler import create_help_request, respond_to_request
from knowledge_base import update_knowledge_base, get_learned_answers

app = Flask(__name__)

@app.route('/receive_call', methods=['POST'])
def receive_call():
    data = request.json
    response = handle_call(data)
    return jsonify(response)

@app.route('/request_help', methods=['POST'])
def request_help():
    data = request.json
    request_id = create_help_request(data)
    return jsonify({"request_id": request_id})

@app.route('/supervisor/respond', methods=['POST'])
def supervisor_respond():
    data = request.json
    success = respond_to_request(data)
    return jsonify({"success": success})

@app.route('/knowledge_base', methods=['GET'])
def knowledge_base():
    answers = get_learned_answers()
    return jsonify({"learned_answers": answers})

if __name__ == '__main__':
    app.run(debug=True)