X_REPEAT = 9
Y_REPEAT = 15

# loop through amount of rows (Y_REPEAT)
# for each row print two lines
# one line for each top and bottom half of a hexagon

for y in range(Y_REPEAT):
    for x in range(X_REPEAT):
        print(r"/ \_", end="")

    print("")

    for x in range(X_REPEAT):
        print(r"\_/ ", end="")

    print()
