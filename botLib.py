import ctypes


botLib = ctypes.CDLL('C:/Users/Jakin/TeamName/botLib.dll')

def convertBoardToC(board):
    newBoard = 0
    i = 0
    for i in range(4):
        for k in range(4):
            newBoard |= int(board[i][k]) << (4*i)
    return newBoard
    
    # for row in board:
    #     for c in row:
    #         newBoard |= int(c) << (4*i)
    #         i += 1
    # return newBoard


# botLib.add.argtypes = [ctypes.c_int, ctypes.c_int]
# botLib.add.restype = ctypes.c_int

# def add(self, a, b):
#     return self.lib.add(a, b)


#https://stackoverflow.com/questions/145270/calling-c-c-from-python
#https://github.com/nneonneo/2048-ai/blob/master/2048.py#L71
#https://stackoverflow.com/questions/5081875/ctypes-beginner
