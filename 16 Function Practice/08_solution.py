

# def print_kwargs(name, power):
#     print("Name: ", name, " Power: ", power)

# print_kwargs(name="Abhishek",power="lazer")
# print_kwargs(name="Abhishek")
# print_kwargs(name="Abhishek",power="lazer", enemy="Dr. Jackaal")




def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    

print_kwargs(name="Abhishek",power="lazer")
print_kwargs(name="Abhishek")
print_kwargs(name="Abhishek",power="lazer", enemy="Dr. Jackaal")