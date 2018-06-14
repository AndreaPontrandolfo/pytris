def playerChooseNumber(player1, player2):

    playerName = input("Are you " + player1 + " or " + player2 + "?\n")

#    def top_left():
#        return "top_left"
#    def top_center():
#        return "top_center"
#    def top_right():
#        return "top_right"
#    def center_left():
#        return "center_left"
#    def center():
#        return "center"
#    def center_right():
#        return "center_right"
#    def bottom_left():
#        return "bottom_left"
#    def bottom():
#        return "bottom"
#    def bottom_rigth():
#        return "bottom_right"

    choose_number = int(input(playerName + " is playing.\n" + playerName +
                              ", scegli una posizione tra: \n1 per top left, \n2 per top center, \n3 per top_right, \n4 per center left, \n5 per center, \n6 per center right, \n7 per bottom left, \n8 per bottom, \n9 per bottom rigth\n\n"))

    position_on_board(choose_number)


def position_on_board(choose_number):
    switcher = {
        1: "top_left",
        2: "top_center",
        3: "top_right",
        4: "center_left",
        5: "center",
        6: "center_right",
        7: "bottom_left",
        8: "bottom",
        9: "bottom_right",
    }
    # Get the function from switcher dictionary
    chooseNumberF = switcher.get(  # this is a lambda
        choose_number, "\nInvalid position chosen")
    # Execute the function

    print(chooseNumberF)

    return chooseNumberF
