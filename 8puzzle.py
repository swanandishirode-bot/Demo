goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbour(state):
    neighbours = []
    x, y = find_blank(state)

    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbours.append(new_state)

    return neighbours


def astar(start):

    open_list = []
    closed_list = []

    g = 0
    h = heuristic(start)
    f = g + h

    open_list.append((start, g, f))

    while open_list:

        open_list.sort(key=lambda x: x[2])

        current, g, f = open_list.pop(0)

        print("State:")
        for row in current:
            print(row)
        print("------")

        if current == goal:
            print("Goal Reached!")
            return

        closed_list.append(current)

        neighbours = get_neighbour(current)

        for neighbour in neighbours:
            if neighbour not in closed_list:
                g_new = g + 1
                h_new = heuristic(neighbour)
                f_new = g_new + h_new

                open_list.append((neighbour, g_new, f_new))


start = []

print("Enter initial state row wise (use 0 for blank):")

for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

astar(start)