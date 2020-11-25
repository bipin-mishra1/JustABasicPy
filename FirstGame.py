import random as rnd

print("Welcome to the Game,Bruh!")

pl_name = input("Enter your name : ").lower()

pl_age = int(input("Enter your age : "))

print(f"Hello,{pl_name} Your age is {pl_age}")
if pl_age > 18:
    print("You are old enough to play the game")
else:
    print("Sorry,{0} your age is {1} which is less than 18,You are not old enough to play the game!!".format(pl_name,pl_age))
    quit()
wants_to_play = input("Do you want to play?[YES|NO] >> ").lower()

if wants_to_play == 'yes':
    print("Welcome Bruh! Let's Play.....")
    health = 15
    print("Initially your health is : 15")
    rnd_int = rnd.randint(0,1)
    left_or_right = input("Enter choice : Left or Right?(left/right)").lower()
    if(rnd_int == 1 and left_or_right == 'left'):
        chc = input("Do you wanna go to home or near the lake?(home/lake)").lower()
        if chc == 'lake':
            print("Near the lake is shark:>>Health fell down By 5")
            health = health - 5
        else:
            print("You reach near the home")
            chc = input("Now, where you want to go in the room or in the library?(room/library)").lower()
            if(chc == 'room'):
                print("In the room there are gues now you re going to exhaust by the work!")
                health = health - 10
                print("your health gone down by 10 because of exhausting work!")
                if health > 5:
                    pass
                else:
                    print("Not enough health!")
                    quit()
            elif chc == 'library':
                print("You are in healthy envirnonment,\nWhich type of book you wanna read?")
                chc = input("(science/science fiction/story)").lower()
                if chc == 'science':
                    print("great! bruh")
                elif chc == 'science fiction' or chc == 'story':
                    print("You shouldn't")
                    quit()
                health+=5
                print("You got 5 health")
             
    elif rnd_int == 0 and left_or_right == 'left':
        print("""Today is no school du to subday?
        Enter you choice what you wanna do today?
        """)
        chc = input("Play video game or solve some maths?(videogame/maths)").lower()
        if(chc == 'video game'):
            print("You exhausted by nintedno game!Health goes down!....Tatat Bye Bye Khatm")
            quit()
        else:
            print("You choose to reead maths Health goes up!")
            health+=5
            if(health>20):
                print("You won the game!")
                quit()
    elif left_or_right == 'right':
        print("You choose to go right? huh! there is no right path!")
        quit()
elif wants_to_play == 'no':
    print("Have a great times,Bye!")
    quit()
