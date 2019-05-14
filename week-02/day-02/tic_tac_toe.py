# Write a function that takes a filename as a parameter
# The file contains an ended Tic-Tac-Toe match
# We have provided you some example files (draw.txt, win-x.txt, win-o.txt)
# Return "X", "O" or "Draw" based on the input file

def tic_tac_result(filename):
    try:
        chess = []
        file = open(filename,'r')
        for line in file:
            chess.append(line)
        file.close()
        return check_chess(chess)

    except IOError:
        print('cannot open',filename)

def check_chess(chess_lst): # chr is o or x
    if "o" == chess_lst[0][0] == chess_lst[0][1] == chess_lst[0][2]:
        return "o"
    if "o" == chess_lst[1][0] == chess_lst[1][1] == chess_lst[1][2]:
        return "o"
    if "o" == chess_lst[2][0] == chess_lst[2][1] == chess_lst[2][2]:
        return "o"
    if "o" == chess_lst[0][0] == chess_lst[1][0] == chess_lst[2][0]:
        return "o"
    if "o" == chess_lst[0][1] == chess_lst[1][1] == chess_lst[2][1]:
        return "o"
    if "o" == chess_lst[0][2] == chess_lst[1][2] == chess_lst[2][2]:
        return "o"
    if "o" == chess_lst[0][0] == chess_lst[1][1] == chess_lst[2][2]:
        return "o"
    if "o" == chess_lst[0][2] == chess_lst[1][1] == chess_lst[2][0]:
        return "o"

    if "x" == chess_lst[0][0] == chess_lst[0][1] == chess_lst[0][2]:
        return "x"
    if "x" == chess_lst[1][0] == chess_lst[1][1] == chess_lst[1][2]:
        return "x"
    if "x" == chess_lst[2][0] == chess_lst[2][1] == chess_lst[2][2]:
        return "x"
    if "x" == chess_lst[0][0] == chess_lst[1][0] == chess_lst[2][0]:
        return "x"
    if "x" == chess_lst[0][1] == chess_lst[1][1] == chess_lst[2][1]:
        return "x"
    if "x" == chess_lst[0][2] == chess_lst[1][2] == chess_lst[2][2]:
        return "x"
    if "x" == chess_lst[0][0] == chess_lst[1][1] == chess_lst[2][2]:
        return "x"
    if "x" == chess_lst[0][2] == chess_lst[1][1] == chess_lst[2][0]:
        return "x"
    return "draw"
    
test_chess = [["o","x","o"],
              ["x","x","x"],
              ["x","x","o"]
            ]

print(tic_tac_result("C:/Users/Ray_Zhang/greenfox/Unicorn-raya/week-02/day-02/win-o.txt"))
# Should print "O"

print(tic_tac_result("C:/Users/Ray_Zhang/greenfox/Unicorn-raya/week-02/day-02/win-x.txt"))
# Should print "X"

print(tic_tac_result("C:/Users/Ray_Zhang/greenfox/Unicorn-raya/week-02/day-02/win-x.txt"))
# Should print "Draw"