#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.strip().endswith('.') or self.value.strip().endswith('?') or self.value.strip().endswith('!')

    def is_question(self):
        return self.value.strip().endswith('?')

    def is_exclamation(self):
        return self.value.strip().endswith('!')

    def count_sentences(self):
        sentences = 0
        for char in self.value:
            if char in ['.', '?', '!']:
                sentences += 1
        return sentences
