# BRUTE FORCE
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        clean_card_num = self.card_num.replace(' ','')
        if len(clean_card_num) <= 1 or not clean_card_num.isdigit():
            return False
        card_num_list = []
        for char in clean_card_num:
            card_num_list = [int(char)] + card_num_list
        for number in range(1, len(card_num_list), 2):
            if card_num_list[number] * 2 > 9:
                card_num_list[number] = (card_num_list[number] * 2) - 9
            else:
                card_num_list[number] = card_num_list[number] * 2
        return sum(i for i in card_num_list) % 10 == 0