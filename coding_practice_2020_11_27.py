
import random


title = "WHILE LOOP COUNTER VARIABLE PRACTICE GENERATOR"
print(title)
print("=" * len(title))
print()

print("""Three steps to looping with a counter variable:
- what is the first value I want to output?
    Set 'i' to that value.
- what is the final value I want to output?
    Include that in the while condition.
- what do I want it to go up by?
    Increase 'i' by that amount.""")

print()

print("Exercises")
print("---------")
print("Create a while loop that will print:")
for n in range(1, 11):
    start = random.randrange(-500, 500)
    times = random.randrange(10, 50)
    by = random.randrange(20)
    print(f"\t{n}. from {start} to {start+times*by} by {by}.")

i = -120
while i <= 40:

  i += 4

i = -12
while i <= 52:

  i += 2

i = -470
while i <=-240:

  i += 10

i = -471
while i <=215:

  i +=14

i = -76
while i <=32:

  i += 9

i = -130
while i <=421:
  
  i += 19

i = -283
while i <=-196:

  i += 3

i = 247
while i <=346: 
  i += 3

i = -212
wihle i <=133:
  i += 15

i = -477
while i <=-277:
  i += 10
