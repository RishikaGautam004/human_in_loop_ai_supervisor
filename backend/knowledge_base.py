from db import save_answer, get_all_answers

def update_knowledge_base(question, answer):
    save_answer(question, answer)

def get_learned_answers():
    return get_all_answers()