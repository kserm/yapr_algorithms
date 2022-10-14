def make_matrix(n):
    matrix = []
    for i in range(n):
        line = list(map(int, input().split()))
        matrix.append(line)
    return matrix

    
def find_neighbours(matrix, x, y):
    neighbours = []
    if x > 0:
        up = matrix[x-1][y]
        neighbours.append(up)
    if y < len(matrix[x])-1:
        right = matrix[x][y+1]
        neighbours.append(right)
    if x < len(matrix)-1:
        down = matrix[x+1][y]
        neighbours.append(down)
    if y > 0:
        left = matrix[x][y-1]
        neighbours.append(left)
    return sorted(neighbours)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = make_matrix(n)
    x = int(input())
    y = int(input())
    print(*find_neighbours(arr, x, y), end=' ')
