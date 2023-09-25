class PrintResult:

    def __init__(self):
        self.__res = 0
        self.__num_moves = 0

    def get_res(self):
        return self.__res

    def get_num_moves(self):
        return self.__num_moves

    def set_res(self, value):
        self.__res = value

    def set_num_moves(self, value):
        self.__num_moves = value

    def del_res(self):
        del self.__res

    def del_num_moves(self):
        del self.__num_moves

    def print_step(self, num_of_step, player1, player2, table):
        print("\nfrom Print_Result After move: ", num_of_step)
        print("User 1:", player1.get_cards_from_user_view())
        print("User 2:", player2.get_cards_from_user_view())
        print("Table :", table.get_cards_from_user_view(), "\n")

    def print_output(self):
        print("The Result is:")
        if self.__res == 1:
            print("Player 1 wins!")
        elif self.__res == 2:
            print("Player 2 wins!")
        else:
            print("It is a tie!")
        print("Number of moves played is ->", self.__num_moves)
