from db import save_request, get_pending_requests, resolve_request

def create_help_request(request_data):
    request_id = save_request({
        "question": request_data.get("question"),
        "status": "pending"
    })
    print(f"Supervisor request logged: {request_id}")
    return request_id

def respond_to_request(response_data):
    request_id = response_data.get("request_id")
    answer = response_data.get("answer")
    
    if resolve_request(request_id, answer):
        print(f"Supervisor answered request {request_id}: {answer}")
        return True
    return False