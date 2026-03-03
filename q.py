import random 

print("14Dec.")
random_num = random.randint(1,100000)
print(random_num)
if random_num % 2 == 0:
    total = random.randint(1,10)
    for i in range(total):
        urgency = random.randint(1,5)
        print(f"Given to S{urgency}")
        project_level = random.randint(1,10)
        print(f"project level is {project_level}")
        print("\n\n")
else:
    print("No projects for today..")