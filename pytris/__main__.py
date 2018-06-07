import sys


def main(args=None):
    print('This is the main.')


if __name__ == '__main__':
    main(sys.argv[1:])


player1 = input("Player1 Tell me your name \n")
player2 = input("Player2 Tell me your name \n")

print("Player1 is " + player1 + " and player2 is " + player2)