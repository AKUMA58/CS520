from collections import deque
import time
from generate_maze import mazeGenerate

maxFringe=0
nodesNum=0
pts=[]

def matrix2graph(matrix):
    # printMap(matrix)
    height = len(matrix)
    width = len(matrix[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if matrix[i][j] == 1}
    for row, col in graph.keys():
        if row < height - 1 and matrix[row + 1][col] == 1:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and matrix[row][col + 1] == 1:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


# find a path like
# "SSEEENNEEEEESSSSWWWSWWNWWSSSEEEEEENEESSS"
def bfsSearch(maze):
    dim = len(maze)
    queue = deque([('', (0, 0))])
    visited = set()
    graph = matrix2graph(maze)

    # test graph
    # print(graph)
    while queue:
        path, current = queue.popleft()
        if current == (dim - 1, dim - 1):
            return path, visited
        if current in visited:
            continue
        visited.add(current)
        if graph.get(current,'null') != 'null':
            for direction, neighbour in graph[current]:
                queue.append((path + direction, neighbour))
    return "NO WAY!"


# parse route like "SSEEENNEEEEESSSSWWWSWWNWWSSSEEEEEENEESSS" into a collection of points
def points(route):
    pts = []
    pts.append((0, 0))
    if (route == 'NO WAY'):
        return pts
    for i in range(0, len(route)):
        cur = pts[i]
        if route[i] == 'S':
            pts.append((cur[0] + 1, cur[1]))
        elif route[i] == 'E':
            pts.append((cur[0], cur[1] + 1))
        elif route[i] == 'N':
            pts.append((cur[0] - 1, cur[1]))
        else:
            pts.append((cur[0], cur[1] - 1))
    return pts


# input: dim wall
# output: path length. nodesNum, maxFringe
def bfs(dim, wall):
    maze = [[1 for col in range(dim)] for row in range(dim)]
    for pt in wall:
        maze[pt[0]][pt[1]] = 0
    if bfsSearch(maze) == 'NO WAY!':
        return [],0,0
    route, visited = bfsSearch(maze)
    maxFringe = fringe(route)
    nodesNum = len(visited)
    pts = points(route)
    return pts, nodesNum, maxFringe


# parse route like "SSEEENNEEEEESSSSWWWSWWNWWSSSEEEEEENEESSS" into a collection of points with maximum length
def fringe(route):
    max = 1
    temp = 1
    direction = ''
    for i in range(0, len(route) - 1):
        if route[i] == route[i + 1]:
            temp = temp + 1
        if temp > max:
            max = temp
            temp = 1
            direction = route[i]
    return max

def run_bfs(dim,wall):
	path, nodes, fringe = bfs(dim,wall)
	if path:
		return path, nodes, fringe
	return ([(0, 0)], 0, 0)

# unit test
# dim = 10
# p = 0.2
# maze, wall = mazeGenerate(dim, p)
# start = time.clock()
# res = bfs(dim, wall)
# end = time.clock()
# print('runtime = ')
# print(end - start)
# if res != 'NO WAY!':
#     pts, nodesNum, maxFringe = res[0], res[1], res[2]
#     print(pts)  # path
#     print(nodesNum)  # number of expanded nodes
#     print(maxFringe)  # maximum of fringe
