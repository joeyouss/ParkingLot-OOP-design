# ParkingLot-OOP-design
Python based OOP design for a parking lot which implements the ideas of abstraction, encapsulation and utilises the heapifying abilities of heap data structure.


## Description of files :
`Inputs.txt` - input for the program
`Polishing_inputs.py` - taking input as a string and distributing it into different commands and making the input ready for processing

`Parking_lot.py` - the main function with every function and class implemented.

## How does it work?
The input file is scanned line by line for input and the first word of every link is treated as a command. A command can be anything like 'park', leave etc.

Then, depending on the command, the relevant function is called which resides in the main function and implements the given functionality.

## Why is heap used?

So the idea of the parking lot was to find the nearest empty spot. To do so we had 2 choices :
1. For each slot in n slots, iterate through the dictionary and find the empty slot
2. Maintain a list of empty slots and return the smallest slot using heap

The first method would in worst case, traverse the who dictionary and hence the time complexity would rise to O(n)
But, maintaining a min heap means we will always have the minimum number of slot available on the top of the heap. Hence, the retrieval will take O(1) since we use pop functionality of heap.

## Error handling :
The code is written in a way to handle the exception of erroneous input using expection handling

## Scalability of this code:
The code can be improved in terms of :
- Better error handling for data type of input
- front end integration. Maintaining a small database on online hosting like heroku etc for a visual effect of the ticketing system
- if a parking lot has multiple floors, inheritance can be used for different floors given that they are implemented using same plan


Thanks for reading!
