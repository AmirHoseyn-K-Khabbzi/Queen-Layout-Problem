import copy , time


#                                                 QUEENS LAYOUT CLASS
# _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_-
class layout(object):

    def __init__(self):
        self.board = [[0 for x in range(Q_num)] for y in range(Q_num)]
        self.num_queens = 0
    def __repr__(self):
        return '\n'.join([''.join(['[Q]' if self.board[x][y]==1 else '[-]' if self.board[x][y]==-1 else '[-]' for x in range(Q_num)]) for y in range(Q_num)])

    def get(self, x, y):
        return self.board[x][y]

    def place_queen(self, x, y):
        assert x in range(Q_num) and y in range(Q_num) and not self.board[x][y]
        self.board[x][y] = 1
        self.num_queens += 1
        for i in range(Q_num):
            if x+i in range(Q_num) and y-i in range(Q_num) and not self.board[x+i][y-i]:
                self.board[x+i][y-i] = -1
            if not self.board[i][y]:
                self.board[i][y] = -1
            if x-i in range(Q_num) and y-i in range(Q_num) and not self.board[x-i][y-i]:
                self.board[x-i][y-i] = -1
#==================================================================================================
            if x+i in range(Q_num) and y+i in range(Q_num) and not self.board[x+i][y+i]:
                self.board[x+i][y+i] = -1
            
            if not self.board[x][i]:
                self.board[x][i] = -1
#==================================================================================================
            if x-i in range(Q_num) and y+i in range(Q_num) and not self.board[x-i][y+i]:
                self.board[x-i][y+i] = -1
            

    def copy(self):
        s = layout()
        s.board = copy.deepcopy(self.board)
        s.num_queens = self.num_queens
        return s
# _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_- _-_-_-_-_-_-_-_-_-_-_-

#                                            THE FIRST MAIN CODE TO RUN

print("PROGRAMMER: AmirHoseyn Khabbazi " +'\n\n' +" Note that number of Queens is mean dimension of chess board" + '\n\n')

print("If there is any problem just let me know to explain, thanks..." + '\n\n')

Q_num = int(input(">> Enter your queens number: "))

if Q_num < 4:
    print("your input number couldnt be less than 4" + '\n' + "Please run program again")
    exit()

if Q_num > 8:
    print("your input number is more than 8 so It may take some time and please wait.....DONT exite program" + '\n\n')

else:
    print("Runing..." + '\n\n')

layout_set = {}


def PickingQueens(Condition=layout()):
    gen = []
    if Condition.num_queens == Q_num:
        sol = str(Condition)
        if sol not in (layout_set):
            layout_set[str(Condition)] = None 
            for i in range(0 ,Q_num):
                for j in range(0 ,Q_num):
                    if Condition.board[i][j] == 1:
                        gen.append(j)
            print("Queens Layout:")
            print (sol + '\n\n' )
            print("Genetic Code: " )
            print( gen)
            print('\n' +"---------- the next solution ----------" + '\n\n')
            gen = []
    else:
        for x in range(Q_num):
            for y in range(Q_num):
                if not Condition.get(x,y):
                    new_Condition = Condition.copy()
                    new_Condition.place_queen(x, y)
                    PickingQueens(new_Condition)


run_time = time.time()

PickingQueens(layout())

print("No more queen layout...")

print ('run time: %.3fs' % (time.time() - run_time))

