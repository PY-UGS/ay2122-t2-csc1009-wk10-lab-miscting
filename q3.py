# Lab 1 question 2b
def Module(module):
    switch={
        "CSC1006": "Mathematics 2",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Strucrture and Algorithms",
        "CSC1009": "Object Oriented Programming",
        "CSC1010": "Computer Networks",
        }
    return switch.get(module,"Unknown Module")


module = input("Enter Module Code: ")
print(Module(module))

print("\n")

# Lab 1 question 2c
for x in range(102, 66, -1):
    if (x % 2 != 0):
        print("The value of x is: ", x)