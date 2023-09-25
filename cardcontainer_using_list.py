#Subclass of CardContainer in which you are asked to use a linked list to represent a deck of cards
from cardcontainer import Card_container
from intcard import Int_card
from node import Node

class Card_container_using_list(Card_container):
    def __init__(self):
        Card_container.__init__(self)
        self.__head = None


    def set_head(self,head):
        self.__head = head

    def get_head(self):
        return self.__head

    def set_innit_num_of_cards(self):
        pass

    # remove first card from list and return it
    def remove_first_card(self):
        if self.__head == None:
            return None
        top_node = self.__head
        self.set_head(top_node.get_next())
        return top_node.get_data()


    # return refrence to first card in cards list
    def get_first_card(self):
        return self.__head.get_data()


    # creates an internal representation of a deck of cards, either owned by player 1, player 2, or on the
    # table, based on a list of cards given by the user view/format.
    # c is the type of card
    def add_new_card(self,c):
        active_node = self.__head
        if self.__head is None:
            self.__head = Node()
            self.__head.set_data(c)
            active_node = self.__head
        while active_node.get_next() is not None:
            active_node = active_node.get_next()
        active_node.set_next(Node())
        active_node.set_data(c)

    #lofc is of list of cards in the user format
    def add_new_cards(self, lofc):
        active_node = self.get_head()
        for card in lofc:
            card_value = self.translate_card_to_internal(card)
            if active_node == self.get_head():
                self.set_head(Node())
                self.__head.set_data(Int_card())
                self.get_first_card().set_value(card_value)
                self.__head.set_next(Node())
                active_node = self.__head.get_next()
            else:
                active_node.set_data(Int_card())
                active_node.get_data().set_value(card_value)
                active_node.set_next(Node())
                active_node = active_node.get_next()

    # Return the list of cards in the internal format
    def get_cards(self):
        internal_format = []
        active_node = self.get_head()
        while active_node is not None:
            internal_format.append(active_node().get_data().get_value())
            active_node = active_node.get_next()
        return internal_format

    # Return the list of cards in the User view format(suit,1-13)
    def get_cards_from_user_view(self):
        user_format = []
        active_node = self.get_head()
        if active_node is not None:
            while active_node.get_next() is not None:
                suit, rank = self.translate_card_to_user(active_node.get_data().get_value())
                user_format.append([suit,rank])
                active_node = active_node.get_next()
            return user_format
        else:
            return []


    def translate_card_to_internal(self,c):
        card_stats = c
        if card_stats[1] == "J":
            card_stats = (card_stats[0],11)
        elif card_stats[1] == "Q":
            card_stats = (card_stats[0],12)
        elif card_stats[1] == "K":
            card_stats = (card_stats[0],13)
        elif card_stats[1] == "A":
            card_stats = (card_stats[0],14)
        if card_stats[0] == "Clubs":
            card_stats = int(card_stats[1]) - 1
        elif card_stats[0] == "Diamonds":
            card_stats = int(card_stats[1]) + 13 - 1
        elif card_stats[0] == "Hearts":
            card_stats = int(card_stats[1]) + 26 - 1
        elif card_stats[0] == "Spades":
            card_stats = int(card_stats[1]) + 39 - 1
        return card_stats



    def translate_card_to_user(self,card_rank):
        suit = ""
        rank = card_rank
        if 1 <= rank <= 13:
            suit = "Clubs"
            rank = rank +1
            if rank ==11:
                rank = "J"
            elif rank ==12:
                rank ="Q"
            elif rank == 13:
                rank = "K"
            elif rank == 14:
                rank = "A"
        elif 14 <= rank <= 26:
            suit = "Diamonds"
            rank = rank + 1 - 13
            if rank ==11:
                rank = "J"
            elif rank ==12:
                rank ="Q"
            elif rank == 13:
                rank = "K"
            elif rank == 14:
                rank = "A"

        elif 27 <= rank <= 39:
            suit = "Hearts"
            rank = rank + 1 - 26
            if rank ==11:
                rank = "J"
            elif rank ==12:
                rank ="Q"
            elif rank == 13:
                rank = "K"
            elif rank == 14:
                rank = "A"
        elif 40 <= rank <= 52:
            suit = "Spades"
            rank = rank + 1 - 39
            if rank ==11:
                rank = "J"
            elif rank ==12:
                rank ="Q"
            elif rank == 13:
                rank = "K"
            elif rank == 14:
                rank = "A"
        return [suit,rank]

