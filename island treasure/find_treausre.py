print("*******************************************************************************")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road_1 = input("you have reached a intersect\n type l for left and r for right").lower
if road_1 == "l":
    river = input("you have reached a river\ntype w to wait or c to cross").lower
    if river == "w":
        door = input("choose one of the three doors\ntype r for red door"
                     "\ntype b for the blue door\ntype y for yellow").lower
        if door == "r":
            print("burned by fire\nGame over")
        elif door == "y":
            print("you win!")
        elif door == "b":
            print("eaten by beast\nGame over!")
        else:
            print("game over")
    else:
        print("attacked by trout!\n Game over")
else:
    print("sorry!, you fall into a hole\n game over!")