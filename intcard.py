from card import Card
#This class gives an internal representation of a card based on the previous description. Note that an integer,
# just like one of those shown at the end of a line below is what an object of IntCard stores as a value.
class Int_card(Card):
    def __init__(self):
        Card.__init__(self)

    def is_Larger_than(self,c):
        new_value = c.get_value()
        self_new_value = self.get_value()
        if 14 <= self_new_value <= 26:
            self_new_value -= 13
        elif 27 <= self_new_value <=39:
            self_new_value -= 26
        elif 40 <= self_new_value <= 52:
            self_new_value -= 39
        if 14 <= new_value <= 26:
            new_value -= 13
        elif 27 <= new_value <=39:
            new_value -=26
        elif 40 <= new_value <= 52:
            new_value -=39
        if self_new_value > new_value:
            return True
        else:
            return False

    def print_card(self):
        if 1 <= self.get_value() <= 13:
            suit = "Clubs"
            rank = self.get_value() + 1
            if rank == 11:
                rank = "J"
            elif rank == 12:
                rank = "Q"
            elif rank == 13:
                rank = "K"
            elif rank == 14:
                rank = "A"
        elif 14 <= self.get_value() <=26:
            suit = "Diamonds"
            rank = self.get_value() + 1
            if rank == 24:
                rank = "J"
            elif rank == 25:
                rank = "Q"
            elif rank == 26:
                rank = "K"
            elif rank ==27:
                rank = "A"

        elif 27 <= self.get_value() <= 39:
            suit = "Hearts"
            rank = self.get_value() + 1
            if rank == 37:
                rank = "J"
            elif rank == 38:
                rank = "Q"
            elif rank == 39:
                rank = "K"
            elif rank == 40:
                rank = "A"

        elif 27 <= self.get_value() <= 39:
            suit = "Hearts"
            rank = self.get_value() + 1
            if rank == 37:
                rank = "J"
            elif rank == 38:
                rank = "Q"
            elif rank == 39:
                rank = "K"
            elif rank == 40:
                rank = "A"

        else:
            suit = "Spades"
            rank = self.get_value() + 1
            if rank == 50:
                rank = "J"
            elif rank == 51:
                rank = "Q"
            elif rank == 52:
                rank = "K"
            elif rank == 53:
                rank = "A"
            print(suit,rank)



