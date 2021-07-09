num_organisms = int(input("Enter the initial number of organisms: "))
rate_growth = float(input("Enter the rate of growth: "))
growth_period = int(input("Enter the number of hours to achieve the rate of growth: "))
total_hours = int(input("Enter the total hours of growth: "))

hours = 0

while hours < total_hours:
    num_organisms *= rate_growth
    hours += growth_period

    # simply to check the data
    print(hours, num_organisms)

    # stops the loop is the next iteration will exceed the max total time allowed
    if hours + growth_period >= total_hours:
        break


print("\nThe total population:", num_organisms)
