# Mini-Excel

**The command line program shall get an input text file with one line, see below example.**
**Each cell can contain numeric value or formula with reference to another cell.**
```
Example:

Input_file: 
2, 18, =2*{0}, 9, ={2}+1*5

Menu:

a. Print current state
b. Change a value

Result:
# a
[0: 2], [1: 18], [2: 4], [3: 9], [4: 25]

# b 0 3 => Cell #0 changed to 3
# a
[0: 3], [1: 18], [2: 6], [3: 9], [4: 35]

# b 2 1 => Cell #2 changed to 1
# a
[0: 3], [1: 18], [2: 1], [3: 9], [4: 10]
```
