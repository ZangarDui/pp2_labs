def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return int(y), int(x)

numheads = 35
numlegs = 94
y, x = solve(numheads, numlegs)
print(f"{y} rabbits : {x} chickens ")