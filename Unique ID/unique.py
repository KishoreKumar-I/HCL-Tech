def unique(lst):
    dict = {}
    unique = []
    for number in lst:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1
    
    for key,value in dict.items():
        if value == 1:
            unique.append(key)

    return unique

lst = list(map(int, input("Enter a list of IDs: ").split()))
print("Unique IDs:", unique(lst))

# Enter a list of IDs: 154 1454 154 954 784 954 
# Unique IDs: [1454, 784]