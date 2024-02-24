

class User:
    def __init__(self, user_id, name, fucks):
        self.user_id = user_id
        self.name = name
        self.fucks = fucks
        self.rank = self.calculate_rank()

    def calculate_rank(self):
        if self.fucks >= 100:
            return "Гуру уебков"
        elif self.fucks >= 75:
            return "Старший уебок"
        elif self.fucks >= 50:
            return "Продвинутый уебок"
        elif self.fucks >= 25:
            return "Младший уебок"
        else:
            return "Новичок"