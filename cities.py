class Cities:
    def __intit__(self, user1, user2_):
        self.user_ids = [user2, user2]
        self.current_step = 1
        self.used_cities = []
        self.last_char = None

    def is_correct_char(self, char):
        return self.last_char is None or self.last_char == char

    def is_unused_city(self, city):
        return city not in self.used_cities

    def change_last_char(self, city):
        bad = ["ъ","ь", "ы", "й", "ё"]
        for i in city[::-1]:
            if i not in bad:
                self.last_char = i
                break


