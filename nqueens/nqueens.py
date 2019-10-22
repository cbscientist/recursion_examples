def placeQueens(board_size, placements=[]):
    """
    A function to define the placement of queens on an NxN
    chessboard such that no queen threatens another.
    """

    # Somehow handle invalid arguments
    # board_size <= 0, board_size = 2, board_size = 3

    board_size = 4  # work with this particular example

    rows = [x + 1 for x in list(range(board_size))]
    cols = [y + 1 for y in list(range(board_size))]

    # [(1,1),(1,2),(1,3),(1,4)]
    # [(2,1),(2,2),(2,3),(2,4)]
    # [(3,1),(3,2),(3,3),(3,4)]        
    # [(4,1),(4,2),(4,3),(4,4)]
    
    if len(placements) < board_size:
        for each_row in rows:
            for each_col in cols:
                placement = (each_row, each_col)
                # check to see if placement valid

                # match_prev
                if placement[1] == previous_placement[0][1]:  # for any previous placement
                    match_col = True
                else:
                    match_col = False

                # match_row = 
                if placement[0] == previous_placement[0][0]:  # for any previous placement
                    match_row = True
                else:
                    match_row = False

                # match_diagonal =   # figure out a way to define this

                if match_row or match_col or 

                if is_valid is True:
                    placements += [placement]
                    placeQueens(board_size, placements)

    else:
        print(placements)


if __name__=="__main__":
    placeQueens(4)