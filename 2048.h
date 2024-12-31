#ifdef __cplusplus
extern "C" {
#endif

#include <bits/stdc++.h>

typedef uint64_t board_t;
typedef uint16_t row_t;

static const board_t ROW_MASK = 0xFFFFULL;
static const board_t COL_MASK = 0x000F000F000F000FULL;

int add(int num, int move);
void myprint(void);

static inline void printBoard(board_t board){
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            uint8_t power = board & 0xf;
            printf("%6u", (power == 0) ? 0 : 1 << power);
            board >>= 4;
        }
        printf("\n");
    }
    printf("\n");
}

static inline board_t unpack_col(row_t row) {
    board_t tmp = row;
    return (tmp | (tmp << 12ULL) | (tmp << 24ULL) | (tmp << 36ULL)) & COL_MASK;
}

static inline row_t reverse_row(row_t row) {
    return (row >> 12) | ((row >> 4) & 0x00F0)  | ((row << 4) & 0x0F00) | (row << 12);
}

#ifdef __cplusplus
}
#endif