class Solver:
    def __init__(self):
        self.__player1 = None
        self.__player2 = None
        self.__table = None
        self.__print_res = None



    def get_player1(self):
        return self.__player1

    def set_player1(self,player1):
        self.__player1 = player1

    def get_player2(self):
        return self.__player2

    def set_player2(self ,player2):
        self.__player2 = player2

    def get_table(self):
        return self.__table

    def set_table(self,table):
        self.__table = table

    def get_print_res(self):
        return self.__print_res
    def set_print_res(self, print_result):
        self.__print_res = print_result

#The solve() method returns(player_number, numberOfSteps).For instance, (1, 30) denotes player 1 wins the game in 30 steps.
# During each step, call the following method to print out each step:
# self.print_result.print_step(c,self.user_1,self.user_2,self.table)

    def solve(self):
        number_of_steps = 0
        war = False
        win = None

        self.__print_res.print_step(number_of_steps, self.__player1,self.__player2,self.__table)
        while win is None and number_of_steps <100:
            if war is False:
                p1_top = self.__player1.remove_first_card()
                p2_top = self.__player2.remove_first_card()
                number_of_steps += 1
                if p1_top.is_Larger_than(p2_top) is True:
                    self.__player1.add_new_card(p1_top)
                    self.__player1.add_new_card(p2_top)
                    self.__print_res.print_step(number_of_steps,self.__player1,self.__player2,self.__table)
                elif p2_top.is_Larger_than(p1_top) is True:
                    self.__player2.add_new_card(p1_top)
                    self.__player2.add_new_card(p2_top)
                    self.__print_res.print_step(number_of_steps,self.__player1,self.__player2,self.__table)
            else:
                number_of_steps += 1
                p1_face_down = self.__player1.removeFirstCard()
                p2_face_down = self.__player2.removeFirstCard()
                self.__table.add_new_card(p1_face_down)
                self.__table.add_new_card(p2_face_down)
                self.__print_res.print_step(number_of_steps, self.__player1, self.__player2, self.__table)

                number_of_steps +=1
                p1_face_up = self.__player1.removeFirstCard()
                p2_face_up = self.__player2.removeFirstCard()
                if p1_face_up.is_Larger_than(p2_face_up) is True:
                    active_node = self.__table.get_head()
                    while active_node.get_next() is not None:
                        self.__player1.add_new_card(active_node.get_data())
                        active_node = active_node.get_next()
                        self.__table.removeFirstCard()
                    self.__player1.add_new_card(p1_face_up)
                    self.__player1.add_new_card(p2_face_up)
                    self.__print_res.print_step(number_of_steps, self.__player1, self.__player2, self.__table)
                    war = False
                elif p2_face_up.is_Larger_than(p1_face_up) is True:
                    active_node = self.__table.get_head()
                    while active_node.get_next() is not None:
                        self.__player2.add_new_card(active_node.get_data())
                        active_node = active_node.get_next()
                        self.__table.removeFirstCard()
                    self.__player2.add_new_card(p1_face_up)
                    self.__player2.add_new_card(p2_face_up)
                    self.__print_res.print_step(number_of_steps, self.__player1, self.__player2, self.__table)
                    war = False
                else:
                    self.__table.add_new_card(p1_face_up)
                    self.__table.add_new_card(p2_face_up)
                    self.__print_res.print_step(number_of_steps, self.__player1, self.__player2, self.__table)
            if self.__player1.get_head().get_data() is None:
                win = 2
            elif self.__player2.get_head().get_data() is None:
                win = 1

        return (win, number_of_steps)













