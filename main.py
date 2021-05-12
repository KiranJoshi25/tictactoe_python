array = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

dictionary = {1: [0,0], 2:[0,1], 3:[0,2],
              4: [1,0], 5:[1,1], 6:[1,2],
              7: [2,0], 8:[2,1], 9:[2,2]}

def check_status():
    if array[0][0] == array[0][1] == array[0][2] or array[1][0] == array[1][1] == array[1][2] \
            or array[2][0] == array[2][1] == array[2][2]:

        return True

    if array[0][0] == array[1][1] == array[2][2] or array[2][0] == array[1][1] == array[0][2]:
        return True

    if array[0][0] == array[1][0] == array[2][0] or array[0][1] == array[1][1] == array[2][1] \
            or array[0][2] == array[1][2] == array[2][2]:

        return True

    else:
        return False


def write_to_array(p,char):
    k,n = dictionary.get(p)

    if array[k][n] == 'X' or array[k][n] == 'O':
        print("invalid input You missed the turn ")
        return False

    else:
        array[k][n] = char

    b = check_status()
    return b

def print_board():

    for i in array:
        print(i)

def check_winner(char,b):

    if char=="X":
        print("player 1 wins")

    else:
        print("player 2 wins")

print_board()


while True:
    p1 = int(input("player1's Turn"))
    b = write_to_array(p1,"X")

    if b is True:
        print("player 1 wins")
        break

    else:
        pass

    print_board()

    p2 = int(input("player2's Turn"))
    b = write_to_array(p2, "O")

    if b is True:
        print("player 2 wins")
        break

    else:
        pass

    print_board()

