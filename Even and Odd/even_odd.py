def even_odd(values):
    even = [value for value in values if value%2==0]
    odd = [value for value in values if value%2!=0]

    # for value in values:
    #     if value%2 == 0:
    #         even.append(value)
    #     else:
    #         odd.append(value)

    print("Even datas of sensor:",even)
    print("Count of even values: ",len(even))
    print("Odd datas of sensor:",odd)
    print("Count of odd values: ",len(odd))

values = list(map(int,input("Enter the sensor data: ").split()))
even_odd(values)


#input : 10 15 20 25 30 35
#output : Even datas of sensor: [10, 20, 30]
#         Count of even values:  3
#         Odd datas of sensor: [15, 25, 35]
#         Count of odd values:  3