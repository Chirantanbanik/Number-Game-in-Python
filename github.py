import random
r = random.randint(1,20)

while(True):
    inp = int(input())
    if(inp<r):
        print("Wrong guess, try a greater number")
    elif(inp>r):
        print("Wrong guess, try a smaller number")
    else:
         print("Congrats, You have guessed the number")
         break;
