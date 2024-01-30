#1
To find the room, the algorithm will first need to check the room number through a user input.

If the room number is between EY 100 and EY 130 (inclusive), proceed to the lab in that room..
If the room number is not within this range, search for all other rooms.

Proceed to explore the rest of the building to find the room among all other rooms.
This algorithm will ensure that we check whether the room falls within the specified range, and if not, it will explore the rest of the building. 

The planning will be like:
Step 1: Check room number.
If step 1 is within range, proceed to step 2:
Step 2: Proceed to the lab in that room.
If step 1 is out of range, proceed to step 3:
Step 3: Search for all other rooms

#2
16 steps. A step here is the number of times we iterate through the room numbers to find the selscted room. Here we take a step to the left and that will be our first step, and then we iterate through 15 rooms to get to EY128. Hence, it will take 16 steps.

#3
This is the worst case scenario. 

#4
For the worst case scenario, if we follow the algorithm, we will have to take left and walk another 15 steps. This will result in 16 steps total to reachthe destination. Whereas, in the best case scenario, if we turned right, it would have taken 7 steps to get to room EY128 in total (1 step to turn right and 6 steps to iterate through the rooms).

#5
To make the algorithm more effective, I would divide the floor plan in two parts at room EY118 and EY120.
The left sign will point towards rooms EY100-EY118. And the sign for right will indicate rooms EY120-EY138. This will make the algorithm more efficient as the number of steps taken to reach EY128 will reduce to 7 from 16.


