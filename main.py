def highest_even(list):
    highest_even = 0
    for item in list:
        if item > highest_even and item % 2 == 0:
            highest_even = item
    return highest_even

print(highest_even([2,5,9,0,-4,8]))
