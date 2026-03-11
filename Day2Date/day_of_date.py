#using build in module datetime

import datetime

def using_datetime(day,month,year):
    try:
        d = datetime.date(year, month, day)
        print(d.strftime("%A"))
        
    except ValueError:
        print("Inavlid date format. Please enter the date in format DD-MM-YYYY")

#using zeller's congurence approach

def zeller_congurence(day,month,year):
    if month <3:
        month+=12
        year -=1

    x = year%100
    y = year//100

    zeller = (day+(13*(month+1))//5 + x + x//4 +y//4 +y*5)%7

    weekdays = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

    print("\n",weekdays[zeller])

while True:
    print("1. Using built-in datetime module Approach")
    print("2. Zeller's congurence Approach")
    print("3. Exit")

    choice = input("Enter your choice of approach: ")

    if choice == "1":
        date_input = input("Enter a date (DD-MM-YYYY): ")
        day,month,year  = map(int, date_input.split("-"))
        using_datetime(day,month,year)

    elif choice == "2":
        date_input = input("Enter a date (DD-MM-YYYY): ")
        day,month,year  = map(int, date_input.split("-"))
        zeller_congurence(day,month,year)

    elif choice == "3":
        print("Exiting..!")
        break

    else:
        print("Invalid Choice.")



# 1. Using built-in datetime module Approach
# 2. Zeller's congurence Approach
# 3. Exit
# Enter your choice of approach: 1
# Enter a date (DD-MM-YYYY): 25-06-2005
# Saturday

# 1. Using built-in datetime module Approach
# 2. Zeller's congurence Approach
# 3. Exit
# Enter your choice of approach: 2
# Enter a date (DD-MM-YYYY): 25-06-2005
# Saturday


