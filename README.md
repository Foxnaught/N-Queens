# N-Queens
This will count the number of ways N-queens can be placed on an NxN chessboard.

n-queens.py was the earliest attempt at implementation and nqueens.c was a port of it to C.
These are both quite slow compared to later attempts.

I later looked online and discovered a bitfield method which uses bitwise operations and integers instead of arrays. This method is much faster.
I implemented these changes in nqueenBitfield.c and then a smaller and slightly faster tinyNQueens.c

tinyNQueens.c should be the fastest implementation.

All versions of the file simply ask for a value of N to be typed into the terminal and then the corresponding number of placements is outputted.
This considers all rotations and mirrorred configurations as unique.
