import unittest
from knowledge_base import update_knowledge_base, get_learned_answers

class TestKnowledgeBase(unittest.TestCase):
    def test_update_knowledge_base(self):
        update_knowledge_base("What services do you offer?", "We provide hair, skin, and spa treatments.")
        answers = get_learned_answers()
        self.assertTrue(any(ans["question"] == "What services do you offer?" for ans in answers))

if __name__ == '__main__':
    unittest.main()