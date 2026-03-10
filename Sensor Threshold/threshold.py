values = list(map(int,input("Enter the sensor values: ").split()))
threshold_value = int(input("Enter the threshold value: "))
filtered_values = [value for value in values if value > threshold_value]

print("Values greater than the threshold are:",filtered_values)