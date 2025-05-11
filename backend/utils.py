def generate_prompt(question):
    """Basic function to generate an AI response."""
    predefined_answers = {
        "What are your business hours?": "We are open from 9 AM to 7 PM.",
        "Do you offer hair styling?": "Yes, we offer a variety of hair styling services."
    }
    
    return predefined_answers.get(question, None)