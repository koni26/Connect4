
#using termcolor for colored shapes
import sys
from termcolor import colored, cprint
#red colored round assigned to red variable and it is for player1
#white colored round assigned to white variable and it is for player2
Red=colored(u'\u2B24', 'red')
White=colored(u'\u2B24', 'white')

#define game table size and its list to store data
rows=8
columns=9
maxrow=12
maxcolumn=18
Storage=[]

#Store data in all rows and columns in Storage list as "   "
#the reason initial value is 3 times space is that round shapes do not fit in one character space.
for i in range(rows):
    Storage.append([])
    for j in range(columns):
        Storage[i].append("   ")

#this function draws table with the data stored in Storage list
def board(r,c):
    #checking if row and column is integer and it blocks if row and column exceeds specified number
    if isinstance(r,int) != True or\
    isinstance(c,int) != True or\
    r<4 and c<4 or r>maxrow or c>maxcolumn:
        return False
    #this loop getting data from Storage list and drawing table with entered rounds each time
    for i in range(columns):
        if i==columns-1:
            if i>9:
                print("  " + str(i+1))
            else:
                print("   " + str(i+1))
        elif i==0:
            print("  " + str(i+1), end="")
        else:
            if i>9:
                print("  " + str(i+1), end="")
            else:
                print("   " + str(i+1), end="")
    for i in range(r*2-1):
        if i%2 == 0:
            for j in range(c):
                if j==c-1:
                    print("|" + Storage[int(i/2)][j] + "|")
                else:
                    print("|" + Storage[int(i/2)][j],end="")
        else:
            for j in range(c):
                if j==c-1:
                    print("-"*5)
                else:
                    print("-"*4,end="")
    for i in range(columns):
        if i==columns-1:
            if i>9:
                print("  " + str(i+1))
            else:
                print("   " + str(i+1))
        elif i==0:
            print("  " + str(i+1), end="")
        else:
            if i>9:
                print("  " + str(i+1), end="")
            else:
                print("   " + str(i+1), end="")
    return True

"""this function is for checking if one of players wins each time then they
typed a column number, if 4 pc of round in one color comes consecutive
(in a row, column or diagonal) then game is over, otherwise goes on"""
def checkgamestatus():
    #first loop is checking if there is a winner in any ROW
    for i in range(rows):
        ConsecutiveRed=0
        ConsecutiveWhite=0
        EndGameRed=False
        EndGameWhite=False
        #if consecutive variables reaches to 4 then game is ending.
        for j in range(columns):
            if Storage[i][j].strip()==Red:
                ConsecutiveRed += 1
                ConsecutiveWhite=0
                if ConsecutiveRed==4:
                    EndGameRed=True
                    return [EndGameRed,EndGameWhite]
            elif Storage[i][j].strip()==White:
                ConsecutiveWhite += 1
                ConsecutiveRed=0
                if ConsecutiveWhite==4:
                    EndGameWhite=True
                    return [EndGameRed,EndGameWhite]
            else:
                ConsecutiveWhite=0
                ConsecutiveRed=0
    #second loop is checking if there is a winner in any COLUMN
    for i in range(columns):
        ConsecutiveRed=0
        ConsecutiveWhite=0
        EndGameRed=False
        EndGameWhite=False
        #if consecutive variables reaches to 4 then game is ending.
        for j in range(rows):
            if Storage[j][i].strip()==Red:
                ConsecutiveRed += 1
                ConsecutiveWhite=0
                if ConsecutiveRed==4:
                    EndGameRed=True
                    return [EndGameRed,EndGameWhite]
            elif Storage[j][i].strip()==White:
                ConsecutiveWhite += 1
                ConsecutiveRed=0
                if ConsecutiveWhite==4:
                    EndGameWhite=True
                    return [EndGameRed,EndGameWhite]
            else:
                ConsecutiveWhite=0
                ConsecutiveRed=0
    #third loop is checking if there is a winner diagonally (row by row)
    for i in range(rows):
        ConsecutiveRed=0
        ConsecutiveWhite=0
        EndGameRed=False
        EndGameWhite=False
        #if consecutive variables reaches to 4 then game is ending.
        startrow=i
        startcol=0
        while startrow < rows and startcol < columns:
            if Storage[startrow][startcol].strip()==Red:
                ConsecutiveRed += 1
                ConsecutiveWhite=0
                if ConsecutiveRed==4:
                    EndGameRed=True
                    return [EndGameRed,EndGameWhite]
            elif Storage[startrow][startcol].strip()==White:
                ConsecutiveWhite += 1
                ConsecutiveRed=0
                if ConsecutiveWhite==4:
                    EndGameWhite=True
                    return [EndGameRed,EndGameWhite]
            else:
                ConsecutiveWhite=0
                ConsecutiveRed=0
            startrow += 1
            startcol += 1
    #fourth loop is checking if there is a winner diagonally (col by col)
    for i in range(columns):
        ConsecutiveRed=0
        ConsecutiveWhite=0
        EndGameRed=False
        EndGameWhite=False
        #if consecutive variables reaches to 4 then game is ending.
        startrow=0
        startcol=i
        while startrow < rows and startcol < columns:
            if Storage[startrow][startcol].strip()==Red:
                ConsecutiveRed += 1
                ConsecutiveWhite=0
                if ConsecutiveRed==4:
                    EndGameRed=True
                    return [EndGameRed,EndGameWhite]
            elif Storage[startrow][startcol].strip()==White:
                ConsecutiveWhite += 1
                ConsecutiveRed=0
                if ConsecutiveWhite==4:
                    EndGameWhite=True
                    return [EndGameRed,EndGameWhite]
            else:
                ConsecutiveWhite=0
                ConsecutiveRed=0
            startrow += 1
            startcol += 1
    #fifth loop is checking if there is a winner diagonally (row by row-reverse)
    for i in range(rows):
        ConsecutiveRed=0
        ConsecutiveWhite=0
        EndGameRed=False
        EndGameWhite=False
        #if consecutive variables reaches to 4 then game is ending.
        startrow=i
        startcol=columns-1
        while startrow < rows and startcol > -1:
            if Storage[startrow][startcol].strip()==Red:
                ConsecutiveRed += 1
                ConsecutiveWhite=0
                if ConsecutiveRed==4:
                    EndGameRed=True
                    return [EndGameRed,EndGameWhite]
            elif Storage[startrow][startcol].strip()==White:
                ConsecutiveWhite += 1
                ConsecutiveRed=0
                if ConsecutiveWhite==4:
                    EndGameWhite=True
                    return [EndGameRed,EndGameWhite]
            else:
                ConsecutiveWhite=0
                ConsecutiveRed=0
            startrow += 1
            startcol -= 1
    #sixth loop is checking if there is a winner diagonally (col by col-reverse)
    for i in range(columns-1,-1,-1):
        ConsecutiveRed=0
        ConsecutiveWhite=0
        EndGameRed=False
        EndGameWhite=False
        #if consecutive variables reaches to 4 then game is ending.
        startrow=0
        startcol=i
        while startrow < rows and startcol > -1:
            if Storage[startrow][startcol].strip()==Red:
                ConsecutiveRed += 1
                ConsecutiveWhite=0
                if ConsecutiveRed==4:
                    EndGameRed=True
                    return [EndGameRed,EndGameWhite]
            elif Storage[startrow][startcol].strip()==White:
                ConsecutiveWhite += 1
                ConsecutiveRed=0
                if ConsecutiveWhite==4:
                    EndGameWhite=True
                    return [EndGameRed,EndGameWhite]
            else:
                ConsecutiveWhite=0
                ConsecutiveRed=0
            startrow += 1
            startcol -= 1
    #seventh loop is checking if there is any empty column
    Emptyslot=0
    Finish= False
    for i in range(columns):
        if Storage[0][i]=="   ":
            Emptyslot += 1
    if Emptyslot == 0:
        Finish=["Yes"]
        return Finish
    return [EndGameRed,EndGameWhite]
    

#assign first player as 1 to start first and its valule equal to zero when its second player's turn
Player1=1
#this is To see which first empty row is; if it remains as "" then asking to select another column
Emptyrow=""

#winner variables to check if there is a winner
Winner1=False
Winner2=False
Status=[]
while True:
    #if winner variable becomes True, it is ending game
    if Winner1==True:
        print("\nGAME OVER, PLAYER1 WINS\n")
        break
    elif Winner2==True:
        print("\nGAME OVER, PLAYER2 WINS\n")
        break
    elif Status==["Yes"]:
        print("\nGAME OVER, NO MORE SLOT! NO WINNER! \n")
        break
    else:
        if Player1==1:
            #starting loop for players to enter col number till game is over.
            while True:
                Emptyrow=""
                selectedColumn=input("\nPlayer1 type col number for "+ Red + " : ")
                print()
                #message for invalid col numbers
                if selectedColumn=="":
                    print("\nInvalid column number, try again!\n")
                    continue
                selectedColumn= int(selectedColumn)
                if selectedColumn > columns or selectedColumn==0:
                    print("\nInvalid column number, try again!\n")
                    continue
                break
            """if there is suitable place to put round then it updates Storage and then draws
                       table with board function"""
            for i in range(rows):
                if Storage[rows-1-i][selectedColumn-1]=="   ":
                    Storage[rows-1-i][selectedColumn-1] = " " + Red + " "
                    Emptyrow=i
                    #update for making it 2nd player's turn
                    Player1=0
                    #draw new look of table
                    board(rows,columns)
                    #Status variable is checking if there is winner with function
                    Status=checkgamestatus()
                    #if there is a winner, winner variable becomes True
                    if True in Status:
                        if Status[0]==True:
                            Winner1=True
                        else:
                            Winner2=True
                    break
            #message if all rows are already filled.
            if Emptyrow=="":
                print("\nNo empty row in this column, try another one!\n")
                continue
            else:
                continue
        else:
            #similar lines for second player
            while True:
                Emptyrow=""
                selectedColumn=input("\nPlayer2 type col number for " + White + " : ")
                print()
                if selectedColumn=="":
                    print("\nInvalid column number, try again!\n")
                    continue
                selectedColumn= int(selectedColumn)
                if selectedColumn > columns or selectedColumn==0 :
                    print("\nInvalid column number, try again!\n")
                    continue
                break
            for i in range(rows):
                if Storage[rows-1-i][selectedColumn-1]=="   ":
                    Storage[rows-1-i][selectedColumn-1] = " " + White + " "
                    Emptyrow=i
                    Player1=1
                    board(rows,columns)
                    Status=checkgamestatus()
                    if True in Status:
                        if Status[0]==True:
                            Winner1=True
                        else:
                            Winner2=True
                    break
            if Emptyrow=="":
                print("\nNo empty row in this column, try another one!\n")
                continue
            else:
                continue
    
