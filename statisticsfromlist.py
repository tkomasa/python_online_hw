lyst = [3, 4, 5, 6, 7, 1, 2]

# make functions for mode, median, and mean for a list
def median(lyst):
    if len(lyst) == 0:
        return 0
    lyst.sort()
    leng = len(lyst)
    median = 0
    if leng % 2 == 0:  # checking if the size of the list is an even number
        median1 = lyst[leng//2]
        median2 = lyst[(leng//2) - 1]
        median = (median1 + median2) / 2
    else:
        median = lyst[leng//2]
    return median


def mode(lyst):
    if len(lyst) == 0:
        return 0
    lyst.sort()
    tempList = []
    i = 0
    while i < len(lyst):
        tempList.append(lyst.count(lyst[i]))
        i += 1
    d1 = dict(zip(lyst, tempList))  # {}
    d2 = {k for (k, v) in d1.items() if v == max(tempList)}
    return d2


def mean(lyst):
    if len(lyst) == 0:
        return 0
    mean = 0
    leng = len(lyst)
    for i in lyst:
        mean += i
    return mean / leng


def main(lyst):



