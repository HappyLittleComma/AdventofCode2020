with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

def getCharacter(r,c):
    char = goToCoord(r, getCyclicCol(r, c))
    return(char)


def getCyclicCol(r, c):
    while c > len(data[r])-1:
        c-=len(data[r])
    return(c)


def goToCoord(r,c):
    col = data[r][c]
    return(col)


def path(downStep, rightStep):
    row=0
    col=0
    trees = 0

    while row<len(data):
        if getCharacter(row, col) == '#':
            trees+=1
        row+=downStep
        col+=rightStep
    return(trees)

#part 1
print(path(1,3))

# part2
print( path(1,1) * path(1,3) * path(1,5) * path(1,7) * path(2,1))
