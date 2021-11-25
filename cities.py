import random


class Cities:
    def __init__(self, user1, user2):
        self.user_ids = [user1, user2]
        self.current_step = random.randint(0, 1)
        self.used_cities = []
        self.last_char = None

    def is_correct_first_char(self, char):
        return self.last_char is None or char.lower() == self.last_char.lower()

    def is_unused_city(self, city):
        return city in self.used_cities

    def change_last_char(self, city):
        bad_letters = ['ы', "ь", "ё", "ъ", "й"]
        for char in city[::-1]:
            if char not in bad_letters:
                self.last_char = char
                break
