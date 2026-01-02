import Creatures
print("Find your information about creatures:examples and characteristics")
while(1):
    print("\nPress\n1. for fish\n2. for birds\n3. for amphibians\n4. for mammals\n5. for reptiles\n6. to exit")
    c=int(input("\nEnter your choice: "))
    if c==1:
        Creatures. Fish.examples()
        Creatures. Fish.chars()
    elif c==2:
        Creatures. Birds.examples()
        Creatures. Birds.chars()
    elif c==3:
        Creatures. Amphibians.examples()
        Creatures. Amphibians.chars()
    elif c==4:
        Creatures. Mammals.examples()
        Creatures. Mammals.chars()
    elif c==5:
        Creatures. Reptiles.examples()
        Creatures. Reptiles.chars()
    elif c==6:
        print("\nThank You!!!")
        break
    else:
        print("Wrong input")
