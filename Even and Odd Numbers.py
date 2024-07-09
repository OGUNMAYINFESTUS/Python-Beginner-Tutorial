# CREATE A LIST OF NATURAL NUMBERS FROM 1 TO 30.
numbers = list(range(1, 30))
# CREATE EMPTY EVEN AND ODD NUMBERS LIST
even_numbers = []
odd_numbers = []
# CREATE A LOOP TO APPEND NUMBERS INTO EACH LIST CREATED ABOVE.
for items in numbers:
    if items % 2 == 0:
        even_numbers.append(items)
    else:
        odd_numbers.append(items)
# PRINT YOUR PROGRAM
print(even_numbers)
print(odd_numbers)


