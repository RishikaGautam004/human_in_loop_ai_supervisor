import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_request(request_data):
    request_ref = db.collection("requests").document()
    request_ref.set(request_data)
    return request_ref.id

def resolve_request(request_id, answer):
    request_ref = db.collection("requests").document(request_id)
    request_ref.update({"answer": answer, "status": "resolved"})
    return True

def get_pending_requests():
    return [doc.to_dict() for doc in db.collection("requests").where("status", "==", "pending").stream()]

def save_answer(question, answer):
    db.collection("knowledge_base").document().set({"question": question, "answer": answer})

def get_all_answers():
    return [doc.to_dict() for doc in db.collection("knowledge_base").stream()]