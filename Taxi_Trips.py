"""Taxi Trips
Created by Francis Torcuato
27/02/2022
"""


BASE_COST = 10
EXTRA_COST = 2
total_time = 0
total_trip = 0
total_income = 0
name = input("What is the drivers name? ")
trip = input("Would you like to start a new trip? ")
while trip != "No":
    time = int(input("How long in minute did the trip take? "))
    total_trip =+ 1
    total_time = time
    cost = BASE_COST * EXTRA_COST * time
    total_income =+ cost
    print(f"The cost for the trip is {cost} ")
    trip = input("Do you want to start a new trip? ")
average_time = total_time / total_trip
average_cost = total_income / total_trip
print(f"Driver's name: {name}")
print(f"The total time of all trips: {total_time} minutes.")
print(f"The average time of all trips: ${average_time} minutes")
print(f"The total income for the day: ${total_income}")
print(f"The average cost of all trips: ${average_cost}")





    







