my_list = [5, 10, "John", 3.14, "Festus", 15, 20, 30, 0.25]
print(my_list[2])
print(my_list[0:5])
print(my_list[5:9])

# ADDING ELEMENTS TO A LIST IN PYTHON USING APPEND () METHOD
# Append method adds elements to the end of a list.
languages = []
languages.append("Python")
languages.append("JavaScript")
languages.append("Java")
languages.append("PHP")
languages.append("SQL")
languages.append("C++")
languages.append("C#")
languages.append("HTML")
languages.append("CSS")
print(languages)

# ADDING A LIST OF ITEMS TO AN EXISTING LIST.
my_class = ["Amanda", "Olubo", "Isabel", "Ethan", "Nnamdi"]
my_class.append(["Folakem", "Osunkoya", "Israel", "Jasmine", "Sochika"])
print(my_class)

# ADDING ELEMENTS TO A LIST USING THE INSERT () METHOD.
# Insert () method adds elements to a specific position in a list.
my_siblings = []
my_siblings.insert(0, "Tomola Ogunmayin")
my_siblings.insert(7, "Festus Ogunmayin")
my_siblings.insert(4,"Esther Okunomo")
my_siblings.insert(1, "Abiodun Ogunmayin")
my_siblings.insert(2, "Veronika Admuwagun")
my_siblings.insert(6, "Funmilayon Metobemu")
my_siblings.insert(3, "Olorunwa Ogunmayin")
my_siblings.insert(6, "Shola Ogunmayin")
print(my_siblings)


# MERGING A LIST OF ITEMS USING EXTEND () METHOD
# Extend () method adds all items of one list to another list.
girls = ["Sochika", "Amanda", "Folakemi", "Isabel", "Jasmine"]
boys = ["Nnamdi", "Ethan", "Osunkoya", "Olubo", "Israel"]
girls.extend(boys)
print(girls)