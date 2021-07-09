import math

smaller = int(input("Smaller: "))
larger = int(input("Larger: "))
max_attempt = math.ceil(math.log(larger-smaller))
count = 0


while count != max_attempt:
    count += 1
    guess = int((larger + smaller)/2)
    print("My guess is: ", guess)
    player_inp = input("enter =, <, >: ")
    if player_inp == '<':
        smaller = guess + 1
    elif player_inp == '>':
        larger = guess - 1
    elif player_inp == '=':
        print("Hooray, we got it in", count, "tries.")
        break
else:
    print("You cheated.")



