theBoard = {'topl': ' ', 'topm': ' ', 'topr': ' ',
            'midl': ' ', 'midm': ' ', 'midr': ' ',
            'lowl': ' ', 'lowm': ' ', 'lowr': ' '}
def printBoard(board):
    print(board['topl'] + '|' + board['topm'] + '|' + board['topr'])
    print('-+-+-')
    print(board['midl'] + '|' + board['midm'] + '|' + board['midr'])
    print('-+-+-')
    print(board['lowl'] + '|' + board['lowm'] + '|' + board['lowr'])

#isWinner = 0    
#def checkForWinner(isWinner):
#    if (theBoard['topl'] and theBoard['topm'] and theBoard['topr']) == 'X' or (theBoard['topl'] and theBoard['topm'] and theBoard['topr']) == 'O':
#        isWinner = 1
#        return isWinner
#    elif (theBoard['midl'] and theBoard['midm'] and theBoard['midr']) == 'X' or (theBoard['midl'] and theBoard['midm'] and theBoard['midr']) == 'O':
#        isWinner = 1
#        return isWinner

markSet = set (['X', 'O'])
turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    while theBoard[move] in markSet:
        print('The space is already taken. Please select another space.')
        move = input()
    theBoard[move] = turn
#    checkForWinner(isWinner)
    if (theBoard['topl'] and theBoard['topm'] and theBoard['topr']) == 'X' or (theBoard['topl'] and theBoard['topm'] and theBoard['topr']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['midl'] and theBoard['midm'] and theBoard['midr']) == 'X' or (theBoard['midl'] and theBoard['midm'] and theBoard['midr']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['lowl'] and theBoard['lowm'] and theBoard['lowr']) == 'X' or (theBoard['lowl'] and theBoard['lowm'] and theBoard['lowr']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['topl'] and theBoard['midl'] and theBoard['lowl']) == 'X' or (theBoard['topl'] and theBoard['midl'] and theBoard['lowl']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['topm'] and theBoard['midm'] and theBoard['lowm']) == 'X' or (theBoard['topm'] and theBoard['midm'] and theBoard['lowm']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['topr'] and theBoard['midr'] and theBoard['lowr']) == 'X' or (theBoard['topr'] and theBoard['midr'] and theBoard['lowr']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['topl'] and theBoard['midm'] and theBoard['lowr']) == 'X' or (theBoard['topl'] and theBoard['midm'] and theBoard['lowr']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif (theBoard['topr'] and theBoard['midm'] and theBoard['lowl']) == 'X' or (theBoard['topr'] and theBoard['midm'] and theBoard['lowl']) == 'O':
        print('We have a winner! Congrats player', turn,'!')
        break
    elif turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
