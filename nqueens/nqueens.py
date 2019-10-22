def placeQueens(board_size, placements=[]):
    """
    A function to define the placement of queens on an NxN
    chessboard such that no queen threatens another.
    """
    if board_size <=0 or board_size==2 or board_size==3:
        raise Exception("Invalid argument: no solution for negative values or for boards where N=2 or N=3.")

    rows = [x + 1 for x in list(range(board_size))]
    cols = [y + 1 for y in list(range(board_size))]

    for row in board_size:
        for col in board_size:
            if len(placements) < board_size:
                # placement in an NxN matrix
                # individually place values using tuple (1...N, 1...N)
                
                placement = (rows[row], cols[col])

                if placement is valid:  # TODO: figure out comparison logic here
                    placements += [placement]
                    placeQueens(board_size, placements)

            else:
                print(placements)

if __name__=="__main__":
    placeQueens(4)