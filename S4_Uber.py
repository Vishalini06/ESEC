n = int(input())

total_time = 0.0
x, y = 0, 0  


for _ in range(n):
    distance, speed, direction = input().split()
    distance = float(distance)
    speed = float(speed)
    
   
    total_time += (distance / speed)  

   
    if direction == 'N':
        y += distance
    elif direction == 'S':
        y -= distance
    elif direction == 'E':
        x += distance
    elif direction == 'W':
        x -= distance


if x > 0 and y > 0:
    final_direction = "NE"
elif x > 0 and y < 0:
    final_direction = "SE"
elif x < 0 and y > 0:
    final_direction = "NW"
elif x < 0 and y < 0:
    final_direction = "SW"
elif x == 0 and y > 0:
    final_direction = "N"
elif x == 0 and y < 0:
    final_direction = "S"
elif y == 0 and x > 0:
    final_direction = "E"
elif y == 0 and x < 0:
    final_direction = "W"
else:
    final_direction = "N" 

# Print the results
print(f"{total_time:.2f}")
print(final_direction)



"""You are working on an app for a company like Uber. You will be provided with the number of laps that the user has taken and travel details (distance, speed and direction) of the laps. Write a program that calculates the total duration of the trip and also the direction in which the customer has travelled.

Input

1. First line of the input will be the number of laps.

 2. The rest of the lines in the input will contain entry in the format of "Distance Speed Direction" for each lap.

Output

1. First line of the output should show the total duration of the trip in minutes (T).

 2. Second line of the output should show the direction from the starting point (D).

Constraints

1. Possible values of input direction are N, E, W, S

N- North 

E-East

W-West

S-South

2. Possible values of output direction are (N, E, W, S, NE, NW, SE, SW)

N - North

W-West

S-South

NE- North East 

NW-North West

 SW - South West
SE - South East

NOTE: Consider 2 digits after decimal point.

For example:

Input	Result
5
5 10 N 
5 10 E
5 10 W
5 10 S
5 10 N
2.50
N

approach and code""
