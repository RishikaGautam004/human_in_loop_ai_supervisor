import livekit
from utils import generate_prompt

def handle_call(call_data):
    query = call_data.get("question", "")
    response = generate_prompt(query)
    
    if response is None:
        return {"message": "Let me check with my supervisor and get back to you.", "request_help": True}
    
    return {"message": response}