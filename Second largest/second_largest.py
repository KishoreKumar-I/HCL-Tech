def second_largest(values):
    if len(values)<2:
        print("At least two values are required.")

    maximum = float('-inf')
    first = second = maximum
    for value in values:
        if value > first:
            second = first
            first = value
        elif value > second and value!=first:
            second = value

    return second

values = list(map(int,input("Enter the values: ").split()))
print("Second largest value is:",second_largest(values))

# Enter the values: 54 95 49 85 76 101 7
# Second largest value is: 95