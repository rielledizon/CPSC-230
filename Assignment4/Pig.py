# pig
import random

# score variables
hum_score = 0
comp_score = 0

# boolean
human = True

print ("Follow directions to start playing PIG:")
# game loop conditions
while hum_score < 100 and comp_score < 100:
    # restart roll variable every loop
    roll = 0
    while human:
        choice = input('Do you want to roll "r" or hold "h" ? ')
        print ()
        if choice == "r":
            dice = random.randint(1, 6)
            print ("You rolled a ", dice)
            print ()
            if dice > 1:
                roll += dice
            else:
                print ("It is now the Player 2's turn.")
                print ()
                human = False
        elif choice == "h":
                hum_score += roll
                print ("Your score is ", hum_score)
                print ("Player 2's score is ", comp_score)
                print ()
                human = False
        else:
            print ("That is an invalid input.")
            print ()
    else:
        print ("Player 2 is playing...")
        print ()
        dice = random.randint(1, 6)
        # stop comp when dice is 1 or score is over 20
        while dice > 1 and roll < 20:
            roll += dice
            dice = random.randint(1, 6)
        # score if 20 over
        if roll >= 20:
            comp_score += roll
        print ("Player 2's score is ", comp_score)
        print ("Your score is ", hum_score)
        print ()
        human = True

# print for game over
if hum_score >= 100:
    print ("You win!")
    print ()
else:
    print ("You lose.")
    print ()
print ("Final scores:")
print ("You: ", hum_score)
print ("Player 2: ", comp_score)
