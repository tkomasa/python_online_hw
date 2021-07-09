height = int(input("Enter height of first drop: "))
bounceIndex = float(input("Enter bounce index: "))
numberOfBounces = int(input("Enter number of bounces: "))

distance = 0

while numberOfBounces > 0:
    numberOfBounces -= 1
    distance += height
    height = height * bounceIndex
    distance += height


print("Distance dropped is", distance)
