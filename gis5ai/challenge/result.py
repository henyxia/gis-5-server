import json

class Result:
    correct = False
    result_entries = []

    def __init__(self):
        self.correct = False
        self.result_entries = []

    def NewEntry(self, title, correct, expected, got):
        self.result_entries.append({
            "title": title,
            "correct": correct,
            "expected": expected,
            "got": got,
        })

    def NewConditionalEntry(self, title, condition, expected, got):
        self.NewEntry(
            title=title,
            expected=expected,
            got=got,
            correct=condition,
        )
        return condition
