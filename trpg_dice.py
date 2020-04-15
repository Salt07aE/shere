import random


class diceroll:
    def __init__(self, count, men):
        self.men = men
        self.count = count

    def roll(self):
        men_int = int(self.men)
        count_int = int(self.count)
        result_dice = []
        result_all = 0

        for i in range(count_int):
            result = random.randint(1, men_int)
            result_dice.append(result)
            result_all += result

        return result_dice, result_all

        #print(result_dice)
        #print(result_all)