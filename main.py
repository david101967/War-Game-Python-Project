import sys
from print_result import PrintResult
from cardcontainer_using_list import Card_container_using_list
from solver import Solver

class Main:

    def read_file_input(self,player_1,player_2,f_name):
        try:
            with open(f_name) as my_file:
                all_cards = my_file.readlines()
            p1_lofc = []
            p2_lofc = []
            for line in all_cards:
                p1_lofc.append((line.split(" ")[0].split(",")[0], line.split(" ")[0].split(",")[1]))
                p2_lofc.append((line.split(" ")[1].split(",")[0],line.split(" ")[1].split(",")[1].strip("\n")))
                player_1.add_new_cards(p1_lofc)
                player_2.add_new_cards(p2_lofc)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
    def main(self):
        file_name = input("Please enter the input file for player1 and player2 cards to play War\n")
        p1 = Card_container_using_list()
        p2 = Card_container_using_list()
        self.read_file_input(p1,p2,file_name)
        table = Card_container_using_list()
        solver = Solver()
        solver.set_player1(p1)
        solver.set_player2(p2)
        solver.set_table(table)
        result = PrintResult()
        solver.set_print_res(result)
        res, num_moves = solver.solve()
        result.set_res(res)
        result.set_num_moves(num_moves)
        print("Game Over!\n")
        result.print_output()
if __name__ == '__main__':
    m = Main()
    m.main()




