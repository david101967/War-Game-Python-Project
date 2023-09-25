#value is an attribute that denotes a card’s value in internal view representation. In this version,
# an integer value is assigned to a card based on the aforementioned mapping.
class Card:
    def __init__(self):
        self.__value = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

# compares the current card with the c parameter by their ranks extracted from their __value attributes in internal format,
# when implemented since ranks must be compared
    def is_Larger_than(self,c):
        pass
#print card in user/view
    def print_card(self):
        pass
