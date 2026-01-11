# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def generate_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"
    return table

def Add_tables():
    for i in range(2, 21):
        t = generate_table(i)
        with open(f"tables/Table_{i}.txt", "w") as f:
            f.write(t)

Add_tables()