from classes.Program import Program


class Duck:

    isBonus = False
    positionX = 0
    positionY = 0
    image = ""
    width = round(Program.window_width / 10)
    height = round(Program.window_height / 10)

    def __init__(self, is_bonus=False):
        self.image = Program.create_image_from(Program.image_path["duck"][0], self.width, self.height)
        self.isBonus = is_bonus
        if self.isBonus:
            self.image = Program.create_image_from(Program.image_path["duck"][1], self.width, self.height)

