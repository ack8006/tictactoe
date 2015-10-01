import pprint
import sys


def main():
    size = 3
    pieces = generatePieces(size)
    turn = 'X'
    done = 0 #0, 1tie, 2win
    print 'Input Moves in format "X num"'
    displayBoard(size, range(1, 1+size**2))
    while not done:
        validEntry = False
        data = None
        while not validEntry:
            data = raw_input(turn + "'s Turn \n")
            validEntry = checkInput(turn, pieces, data)
        piece, loc = data.split()
        pieces = makeMove(pieces, piece, loc)
        displayBoard(3, pieces)
        done= checkDone(pieces, size, turn)
        if done:
            if done==1:
                print 'Tie'
            elif done==2:
                print turn + " Wins"
        else:
            turn = nextTurn(turn)


def generatePieces(size):
    return [' ']*(size**2)

def displayBoard(size, pieces):
    lineToPrint = ''
    for ind, val in enumerate(pieces):
        if ind%size == (size-1) and ind >0:
            lineToPrint += str(val)
            print lineToPrint
            if ind < (size**2-1):
                print '------'
            lineToPrint = ''
        else:
            lineToPrint+=str(val)+'|'
    print lineToPrint

def checkInput(turn, pieces, data):
    try:
        piece, loc = data.split()
        if not piece.upper()==turn:
            return False
        elif not pieces[int(loc)-1] ==' ':
            return False
        else:
            return True
    except:
        return False

def makeMove(pieces, piece, loc):
    pieces[int(loc)-1] = piece.upper()
    return pieces

def nextTurn(turn):
    if turn == 'X':
        return 'O'
    else: return 'X'

def checkDone(pieces, size, turn):
    for x in range(0,size):
        if pieces[(0+size*x):(3+size*x)].count(turn) == size:
            print 'row'
            return 2

        if [val for ind, val in enumerate(pieces) if ind in range(x, size**2, size)].count(turn) == size:
            print 'col'
            return 2
    if [x for i,x in enumerate(pieces) if i in range(0, size**2, size+1)].count(turn) == size:
        print 'diag1'
        return 2
    elif [x for i,x in enumerate(pieces) if i in range(size-1, size**2, size-1)].count(turn) == size:
        print 'diag2'
        return 2

    if ' ' not in pieces:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
