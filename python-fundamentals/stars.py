# part 1
def draw_stars(x):
    for i in range(len(x)):
        print x[i] * "*"
draw_stars(x = [4, 5, 1, 3, 5, 7, 25])

# part 2
def draw_stars(x):
    for i in range(len(x)):
        result = isinstance(x[i], int)
        if result == True:
             print x[i] * "*"
        if  result == False:
             print x[i][0] * len(x[i])

draw_stars( x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
