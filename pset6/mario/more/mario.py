from cs50 import get_int


# Main: Getting valid height and then building pyramid
def main():
    height = total_height = get_height()
    pyramid(height, total_height)


# Abstraction: Getting valid positive integer between 1 and 8 inclusive
def get_height():
    while True:
        i = get_int("Height: ")
        if i >= 1 and i <= 8:
            return i
            break


# Abstraction: Recursively building current level of pyramid and building previous level
def pyramid(height, total_height):
    # Base Condition when function comes to building the uppermost block
    if height == 1:
        for i in range(total_height - 1):
            print(" ", end="")
        print("#  #", end="")
        print("")
    # Building current level and building previous level via recursion
    else:
        pyramid(height - 1, total_height)
        for i in range(total_height - height):
            print(" ", end="")
        for i in range(height):
            print("#", end="")
        print("  ", end="")
        for i in range(height):
            print("#", end="")
        print("")


if __name__ == "__main__":
    main()