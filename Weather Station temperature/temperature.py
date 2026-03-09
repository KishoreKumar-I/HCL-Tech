import math
def temperature_analysis(temperatures):
    for i,values in enumerate(temperatures,start=1):
        print(f"Day {i} : {values}°C")

    maximum_temperature = -math.inf
    for value in temperatures:
        if value > maximum_temperature:
            maximum_temperature = value
    print("\nMaximum temperature :",maximum_temperature,"°C")
    minimum_temperature = math.inf
    for value in temperatures:
        if value < minimum_temperature:
            minimum_temperature = value
    print("Minimum temperature :",minimum_temperature,"°C")

    average_temperature = sum(temperatures) / len(temperatures)
    print("Average temperature :",average_temperature,"°C")

print("Enter the temperatures for 7 days :")
temperatures = []
for i in range(7):
    temp = float(input(f"Day {i+1} :"))
    temperatures.append(temp)
temperature_analysis(temperatures)

#input : temperatures = [25,26,27.5,30.5,28,24,32]
#output : Day 1 : 25.0°C
#         Day 2 : 26.0°C
#         Day 3 : 27.5°C
#         Day 4 : 30.5°C
#         Day 5 : 28.0°C
#         Day 6 : 24.0°C
#         Day 7 : 32.0°C
#         Maximum temperature : 32.0°C
#         Minimum temperature : 24.0°C
#         Average temperature : 28.0°C