def unique(lst):
    unique = []
    for number in lst:
        if number not in unique:
            unique.append(number)
    return ", ".join(map(str, unique))

lst = list(map(int, input("Enter a list of IDs: ").split()))
print("Unique IDs:", unique(lst))

# Enter a list of IDs: 154 1454 154 954 784 954
# Unique IDs: 154, 1454, 954, 784