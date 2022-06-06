You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be 
different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by 
‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two coordinates from 
the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y). You can 
move only in the following directions. 
L: move to left cell from the current cell 
R: move to right cell from the current cell 
U: move to upper cell from the current cell 
D: move to the lower cell from the current cell 
 
You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal 
is to reach the destination cells covering the minimum number of cells as you travel from the 
starting cell.  
 
Example Board: 
 
- - - - - 
- - # - - 
- - - - - 
# - # # - 
- # - - - 
 
 
Input: board, source, destination. 
Puzzle: A list of lists, each list represents a row in the rectangular puzzle. Each 
element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable). The same 
as in the example. 
Example:  
Puzzle = [['-', '-', '-', '-', '-'], ['-', '-', '#', '-', '-'], ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-'], ['-', '#', '-', '-', '-']] 
 
source: A tuple representing the indices of the starting position, e.g. for the upper 
right corner, source=(0, 4). 
destination: A tuple representing the indices of the goal position, e.g. for the lower 
right corner, goal=(3, 4). 
 
Output: A list of tuples representing the indices of each position in the path. The first tuple 
should be the starting position, or source, and the last tuple should be the destination. If 
there is no valid path, None should be returned. Not an empty list, but the None object. 
 
Note: The order of these tuples matters, as they encode a path. Each position in the path 
must be empty (correspond to a ‘-’ on the board) and adjacent to the previous position. 
 
(Extra Credit): For the above puzzle in addition to the output return the directions as well in 
the form of a string. 
