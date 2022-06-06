# Author: Tina Kuran
# Date: 5/31/2022
# Description: CS325 Spring 2022 Portfolio Project - Graph Traversal Puzzle

import heapq


def solve_puzzle(board, source, destination):
    """
    You are given a 2-D puzzle of size MxN, that has N rows and M column
    (N>=3 ; M >= 3; M and N can be different). Each cell in the puzzle is
    either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen)
    and the one with a barrier is marked by ‘#’. You are given two coordinates
    from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want
    to reach (x,y). You can move only in the following directions.
        L: move to left cell from the current cell
        R: move to right cell from the current cell
        U: move to upper cell from the current cell
        D: move to the lower cell from the current cell

    You can move to only an empty cell and cannot move to a cell with a barrier
    in it. Your goal is to reach the destination cells covering the minimum number
    of cells as you travel from the starting cell.
    """
    rows, cols = len(board), len(board[0])
    s_row, s_col = source[0], source[1]
    d_row, d_col = destination[0], destination[1]

    # Initialize a 2D array to store the path length to each square.
    dist = [[float("infinity")] * cols for x in range(rows)]
    dist[s_row][s_col] = 0

    # Initialize a 2D array to store the adjacent square that was used to get
    # to a specific square via the shortest path.
    prev = [[None] * cols for x in range(rows)]

    # Initialize a priority queue: distance, row, column of the source.
    pq = [(0, s_row, s_col)]

    # While priority queue is not empty, pop and investigate.
    while len(pq) > 0:
        cur_dist, row, col = heapq.heappop(pq)

        # Only visit each square once.
        if cur_dist > dist[row][col]:
            continue

        # Identify neighbor positions.
        neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
        for n_row, n_col in neighbors:
            # Check if the neighbor is valid and not a blocked square.
            if (0 <= n_row < rows and 0 <= n_col < cols) and \
                    board[n_row][n_col] != "#":
                temp_dist = cur_dist + 1

                # New distance should only be considered if it is better than one already found.
                if temp_dist < dist[n_row][n_col]:
                    dist[n_row][n_col] = temp_dist
                    prev[n_row][n_col] = (row, col)
                    heapq.heappush(pq, (temp_dist, n_row, n_col))

    # If the destination is not reachable, return None.
    if dist[d_row][d_col] == float("infinity"):
        return None

    # Otherwise call function that returns path.
    return solve_puzzle_path(destination, prev)


def solve_puzzle_path(destination, prev):
    """
    Helper function that determines the sequence of squares that were
    visited in order to form the shortest path from source to destination.
    """
    # Initialize current square, list to store the square coordinates, and
    # an empty string to store the direction of the path.
    cur = destination
    puzzle_path = []
    directions = ""

    # Start at the destination and work backwards until the source is reached.
    while cur is not None:
        puzzle_path.append(cur)
        temp = cur
        cur = prev[cur[0]][cur[1]]

        # Determine the what direction was taken in order to create the path
        # between the current square and the previous square.
        if cur is not None:
            directions = solve_puzzle_directions(directions, temp, cur)

    return puzzle_path[::-1], directions[::-1]


def solve_puzzle_directions(directions, pre, cur):
    """
    Helper function that determines the direction the path took at each move.
    """
    if pre[0] == cur[0] - 1:
        directions += "U"
    elif pre[0] == cur[0] + 1:
        directions += "D"
    elif pre[1] == cur[1] - 1:
        directions += "L"
    elif pre[1] == cur[1] + 1:
        directions += "R"

    return directions
