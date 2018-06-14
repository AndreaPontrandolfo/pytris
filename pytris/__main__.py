import sys
from TicTacToeLib import playerChooseNumber

def main(args=None):

    player1 = (input("Player1 Tell me your name \n")).capitalize()
    player2 = (input("Player2 Tell me your name \n")).capitalize()

    print("Player1 is " + player1 + " and player2 is " + player2 + "\n")

    playerChooseNumber(player1, player2)

if __name__ == '__main__':
    main(sys.argv[1:])


