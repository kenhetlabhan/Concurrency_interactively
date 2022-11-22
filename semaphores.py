import numpy as np
import random

def main():
    print("""Welcome to moonstones. This program uses the closest neighbour algorithm to find the shortest route between different randomly generated stones on a moon.""")
    moonSize, moon, stones = get_moon()
    print(stones)
    print(len(stones))
    steps, distance, to_go, current_stone= get_distance(stones)
    moon_with_route = make_Route(steps, moonSize)

    print(f"This is the original moon\n{moon}")
    print(f"These are the steps taken:  {steps}")
    print(f"The shortest path to get to the stones is {len(steps) - 1} steps.")

    print(f"This is the moon again but with the route noted:\n {moon_with_route}")
def make_Route(steps, moonSize):
    i = 0
    moon_with_route = np.zeros((moonSize, moonSize)) #makes an array like moon. But filled with only zeros.
    for coordinate in steps:

        moon_with_route[steps[i][1], steps[i][0]] += 1 #goes through every coordinate in steps and increments every coordinate in moon_with_route with 1 if the robot visits the coordinate.
        i += 1


    return moon_with_route

def get_distance(stones):
    current_stone = [0,0] #coordinates to keeps track where the robot is.
    to_go = [0,0]
    steps = [[0, 0]] #steps is a list of coordinates that the robot takes.
    distance = []
    counter = 0

    while len(stones) > 0: #runs the algorithm until the list with the coordinates of the stones is empty.

        distance = []
        for coordinate in range(0, len(stones)):
            distance.append([abs(stones[coordinate][0] - current_stone[0]) + abs(stones[coordinate][1] - current_stone[1]), coordinate]) #Writes for every element in the list stones the distance, and which number of element it is. For Example [4,3] means stone number the distance from current position to stone number 3 is 4.


        distance.sort()# sorts the list for the shortest distance first.

        to_go[0] = stones[distance[0][1]][0] #sets the x coordinate of the stone to go to to the x coordinate of the stone with the shortest distance.
        to_go[1] = stones[distance[0][1]][1] #sets the x coordinate of the stone to go to to the y coordinate of the stone with the shortest distance.


        while steps[-1][0] < to_go[0]:
            steps.append([steps[-1][0] + 1, steps[-1][1]])
        while steps[-1][1] < to_go[1]:
            steps.append([steps[-1][0], steps[-1][1] + 1])
        while steps[-1][0] > to_go[0]:
            steps.append([steps[-1][0] - 1, steps[-1][1]])
        while steps[-1][1] > to_go[1]:
            steps.append([steps[-1][0], steps[-1][1] - 1])
        current_stone = [steps[-1][0],steps[-1][1]] #sets the coordinate of the current_stone to the element in the list of steps.

        stones.pop(distance[0][1]) # It removes the element in the list stones which the robot visited.




    return steps, distance, to_go, current_stone

# You get this function for free to retrieve the size of the moon from the user. You're free to write your own!
def get_moon():
    print("On what moon size do you want your robot to search (5, 6, 7 or 8)? ")
    moonSize = input(">>   ")

    try:
        moonSize = int(moonSize)
        if moonSize in [5, 6, 7, 8]:
            print(f"How many stones do you want the moon to have?, the maximum is {moonSize*moonSize-1}")
            amount_Stones = input(">>  ")
            try:
                amount_Stones = int(amount_Stones)
                if amount_Stones <= moonSize*moonSize - 1 and amount_Stones >= 0:

                    moon = np.zeros((moonSize, moonSize)) #creates an array which holds the amount of elements of the input which each also holds that amount of elements.
                    stones = [] #makes an empty list containing coordinates in a seperate list.

                    while ((moon == 1).sum() < amount_Stones) and moon[0,0] != 1: # This loop runs until 2 elements have been changed to 1. And the element [0, 0] can't be 1.


                        y_coord_number = random.randint(0, moonSize-1)
                        x_coord_number = random.randint(0, moonSize-1)
                        moon[y_coord_number, x_coord_number] = 1 # sets an random element in the moon array from 0 to 1

                        if moon[0, 0] == 1:
                            moon[0, 0] = 0
                        else:
                            stones.append([x_coord_number, y_coord_number])


                    stones_without_duplicates = []
                    for element in stones:
                        if element not in stones_without_duplicates:
                            stones_without_duplicates.append(element) #If an element is not yet in this new list, it will append it to the new list. The new list will eventually contain the coordinates of all stones without duplicates.

                    stones = stones_without_duplicates
                    return moonSize, moon, stones



                elif amount_Stones > moonSize*moonSize - 1:
                    print("Your input of stones is too big!!")
                    return get_moon()
                elif amount_Stones < 0:
                    print("Your input of stones is too small!!")
                    return get_moon()

                else:
                    print("Your input of stones is invalid")
                    return get_moon()
            except:
                print("Your input of stones is invalid")
                return get_moon()
        elif moonSize > 8:
            print("Your moon size is too big!!")
            return get_moon()
        elif moonSize < 5:
            print("Your moon size is too small!!")
            return get_moon()
        else:
            print("Your moon size input is invalid!")
            return get_moon()
    except:
        print("Your moon size input is invalid!")
        return get_moon()

# This makes sure that the program start running with the main() function
if __name__ == "__main__":
    main()
