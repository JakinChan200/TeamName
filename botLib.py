import ctypes


botLib = ctypes.CDLL('C:/Users/Jakin/TeamName/botLib.dll')

botLib.init_tables()

# botLib.find_best_move.argtypes = [ctypes.c_uint64]
# botLib.score_toplevel_move.argtypes = [ctypes.c_uint64, ctypes.c_int]
# botLib.score_toplevel_move.restype = ctypes.c_float
# botLib.execute_move.argtypes = [ctypes.c_int, ctypes.c_uint64]
# botLib.execute_move.restype = ctypes.c_uint64

def to_c_board(m):
    board = 0
    i = 0
    for row in m:
        for c in row:
            board |= int(c) << (4*i)
            i += 1
    return board

def from_c_board(n):
    board = []
    i = 0
    for ri in range(4):
        row = []
        for ci in range(4):
            row.append((n >> (4 * i)) & 0xf)
            i += 1
        board.append(row)
    return board

def to_c_index(n):
    return [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768].index(n)

def from_c_index(c):
    if c == 0: return 0
    return 2**c
    
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
