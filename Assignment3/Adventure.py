# choose your own adventure: enchanted wizard

import random

# forced to begin intro room
next_room = 1
choice = ""

while next_room != 0:
    # random death generator resets each time the loop starts
    death = random.randint(1, 100)

    # intro room
    if next_room == 1:
        # intro to story; redirect room to not reprint intro
        print ('You were walking in the Enchanted Forest when'
               'a wizard apparates infront of you.\n'
               'He is looking for an able apprentice and believes that'
               'you may be worthy enough\nto be his right-hand man. '
               'He says, "Those worthy to find the Acacia wand and\ndefeat '
               'the Lion Dragon are welcome to become my students." You, '
               'being very\ncurious and eager, agree to his challenge. He '
               'presents you with two choices to\nstart the task: Enter the '
               'vortex he conjured or ride the pegasus he formed out\nof the '
               'clouds')
        print ()
        next_room = 2

    # room 2
    elif next_room == 2:
        choice = input('What do you choose? "vortex" or "pegasus" ? ')
        print ()
        if choice == "vortex":
            if death > 98:
                print ("The wizard wants an apprentice that can make quick "
                       "connections with the animals of\nthe universe. The "
                       "vortex was to see if you were too untrustworthy of "
                       "wild\ncreatures. The vortex transports you to the "
                       "middle of space. With no source of oxygen,\nyou die "
                       "floating in the black abyss.")
                print ()
                next_room = 100
            else:
                print ("The vortex transports you to the lakeside. "
                       "You see a boat.")
                print ()
                next_room = 1.1
        elif choice == "pegasus":
            print ("You approach the pegasus and it lets you climb aboard. "
                   "The pegasus flies high\nand takes you to the mystical "
                   "cloud kingdom. You see a cloud castle and a"
                   "\ncloud garden.")
            print ()
            next_room = 1.2
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "vortex" and choice != "pegasus"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do you"
                               ' choose? "vortex" or "pegasus" ? ')
                print ()
                count += 1
                if choice == "vortex":
                    print ("The vortex transports you to the lakeside. "
                           "You see a boat.")
                    print ()
                    next_room = 1.1
                else:
                    print ("You approach the pegasus and it lets you climb "
                           "aboard. The pegasus flies high\nand takes you to "
                           "the mystical cloud kingdom. You see a cloud castle"
                           " and a\ncloud garden.")
                    print ()
                    next_room = 1.2

    # choice: vortex (1.1)
    elif next_room == 1.1:
        choice = input('Do you wish to use the "boat" or return to the '
                       '"vortex" ? ')
        print ()
        if choice == "boat":
            if death > 98:
                print ("As you paddle your way across the lake, bubbles begin "
                       "to form underneath your boat. Out of nowhere, a lake "
                       "dragon begins to emerge, mouth wide, swallowing you "
                       "and the boat whole.")
                print ()
                next_room = 100
            else:
                print ("You paddle across the lake and reach the shore of "
                       "skull rock. You see a pirate\n"
                       "ship docked close by and a path inside the cave.")
                print ()
                next_room = 2.11
        elif choice == "vortex":
            print ("You reappear in the Enchanted Forest with the wizard's "
                   "initial options.")
            print ()
            next_room = 2
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "boat" and choice != "vortex"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do you"
                               ' choose? "boat" or "vortex" ? ')
                print ()
                count += 1
            if choice == "boat":
                print ("You paddle across the lake and reach the shore of "
                       "skull rock. You see a pirate\nship docked close "
                       "by and a path to a cave.")
                print ()
                next_room = 2.11
            else:
                print ("You reappear in the Enchanted Forest with the wizard's"
                       " initial options.")
                print ()
                next_room = 2

    # choice: pegasus (1.2)
    elif next_room == 1.2:
        choice = input('Do you decide to take light, careful steps to the '
                       '"castle" or the "garden" ? ')
        print ()
        if choice == "castle":
            if death > 80:
                print ("You did not step light enough. Your heavy steps made "
                       "a cloud give in. You fall\nfrom the sky, your "
                       "body splatting on the ground.")
                print ()
                next_room = 100
            else:
                print ("You enter the gates of the castle and see the king "
                       "seated on his throne meters\naway from the door.")
                print ()
                next_room = 2.21
        elif choice == "garden":
            print ("You do not realize that the path to the garden is "
                   "dangerous and full of cloud\nholes. You misstep and fall "
                   "through the clouds from the sky. You hear the\nvoice of "
                   'the wizard from above saying , "What a lost cause..."'
                   "You close your\neyes as your fall ends with you splatting "
                   "on jagged rocks, the high tide waves\ncrashing on the "
                   "rocks, washing your splattered body away.")
            print ()
            next_room = 100
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "castle" and choice != "garden"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do you"
                               ' choose? "castle" or "garden" ? ')
                print ()
                count += 1
            if choice == "castle":
                if death > 80:
                    print ("You did not step light enough. Your heavy steps "
                           "made a cloud give in. You fall\nfrom the sky, your"
                           " body splatting on the ground.")
                    print ()
                    next_room = 100
                else:
                    print ("You enter the gates of the castle and see the king"
                           "seated on his throne meters\naway from the door.")
                    print ()
                    next_room = 2.21
            else:
                print ("You do not realize that the path to the garden is "
                       "dangerous and full of cloud\nholes. You misstep and "
                       "fall through the clouds from the sky. You hear "
                       'the\nvoice of the wizard from above saying , "What a '
                       'lost cause..." You close your\neyes as your fall ends '
                       "with you splatting on jagged rocks, the high tide "
                       "waves\ncrashing on the rocks, washing your splattered "
                       "body away.")
                print ()
                next_room = 100

    # choice: boat (2.11)
    elif next_room == 2.11:
        choice = input('Do you want to approach the pirate "ship" or walk to'
                       ' the "cave"? ')
        print ()
        if choice == "ship":
            print ("You walk the ramp up the ship. You hear snoring in the "
                   "captain's quarters.")
            print ()
            next_room = 3.111
        elif choice == "cave":
            print ("You find an island in the middle of the cave with a "
                   "treasure chest at its center")
            print ()
            next_room = 3.112
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "ship" and choice != "cave"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do you"
                               ' choose? "ship" or "cave" ? ')
                print ()
                count += 1
            if choice == "ship":
                print ("You walk the ramp up the ship. You hear snoring in "
                       "the captain's quarters and\nsee a door to the "
                       "ship's lower deck.")
                print ()
                next_room = 3.111
            else:
                print ("You find an island in the middle of the cave with a "
                       "treasure chest at its center")
                print ()
                next_room = 3.112

    # choice: castle (2.21)
    elif next_room == 2.21:
        choice = input('Do you approach the "king" or go "back" ? ')
        print ()
        if choice == "king":
            if death > 75:
                print ("The king thinks you're an assassin trying to steal "
                       "his throne. He pulls out\na wand you believe to be "
                       "the Acacia wand and casts a spell on you. You "
                       "suddenly\nrealize you can't move. As you see "
                       "your lower body slowly turn into stone, you\nfind "
                       "the king cast a thunder cloud above you. You stand "
                       "there horrified as a\nlightning bolt hurls toward "
                       "the statue that you have become, disintegrating\nyour "
                       "body.")
                print ()
                next_room = 100
            else:
                print ("The king welcomes you to his home and talks about his "
                       "life. As he recounts his\npast, you hear him mention "
                       "the Acacia wand. You question him about it. He "
                       "asks\nwhy, and you tell him of the wizard's task. "
                       "Being kind and generous, the king\nsays you "
                       "may take the wand for your task given you complete "
                       "a certain mission.")
                print ()
                next_room = 3.21
        elif choice == "back":
            print ("You walk out and find yourself in the same area.")
            print ()
            next_room = 1.2
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "king" and choice != "back"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "king" or "back" ? ')
                print ()
                count += 1
                if choice == "king":
                    if death > 75:
                        print ("The king thinks you're an assassin trying to "
                               "steal his throne. He pulls out\na wand you "
                               "believe to be the Acacia wand and casts a "
                               "spell on you. You suddenly\nrealize you can't "
                               "move. As you see your lower body slowly turn "
                               "into stone, you\nfind the king cast a thunder "
                               "cloud above you. You stand there horrified as "
                               "a\nlightning bolt hurls toward the statue that"
                               " you have become, disintegrating\nyour body.")
                        print ()
                        next_room = 100
                    else:
                        print ("The king welcomes you to his home and talks "
                               "about his life. As he recounts his\npast, you "
                               "hear him mention the Acacia wand. You "
                               "question him about it. He asks\nwhy, and you "
                               "tell him of the wizard's task. Being kind and "
                               "generous, the king\nsays you may take the "
                               "wand for your task given you complete a "
                               "certain mission.")
                        print ()
                        next_room = 3.21
                else:
                    print ("You walk out and find yourself in the same area.")
                    print ()
                    next_room = 1.2

    # choice: ship (3.111)
    elif next_room == 3.111:
        choice = input('Do you want to go to the "captain" or go "back" ? ')
        print ()
        if choice == "captain":
            print("You see the captain passed out on his desk. As you almost "
                  "walk back out, a glint\ncatches your eye. You notice a "
                  "shiny silver box tucked under the captain's arm.")
            print ()
            next_room = 4.1
        elif choice == "back":
            print ("You return to the shore of Skull Rock.")
            print ()
            next_room = 2.11
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "captain" and choice != "back"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "captain" or "back" ? ')
                print ()
                count += 1
                if choice == "captain":
                    print("You see the captain passed out on his desk. As you "
                          "almost walk back out, a glint\ncatches your eye. "
                          "You notice a shiny silver box tucked under the "
                          "captain's arm.")
                    print ()
                    next_room = 4.1
                else:
                    print ("You return to the shore of Skull Rock.")
                    print ()
                    next_room = 2.11

    # choice: cave (3.112)
    elif next_room == 3.112:
        choice = input('Do you want to "swim" to the middle or go "back" ? ')
        print()
        if choice == "swim":
            if death > 98:
                print ("As you swim to the middle, you feel something touch "
                       "the bottom of your feet.\nYou hesitate but continue "
                       "swimming. 5 meters away from the shore, you "
                       "feel\nsomething violently grab your leg. As you turn "
                       "your head, you find a demon\nmermaid pulling you "
                       "down, down, down to the bottom of the lake. You try "
                       "to swim to\nthe surface for air but the demon mermaid "
                       "has an iron grip on you.\nYou drown in the darkness "
                       "of the lake cavern.")
                print ()
                next_room = 100
            else:
                print ("You reach the middle and see the treasure chest.")
                print ()
                next_room = 4.1121
        elif choice == "back":
            print ("You return to the lakeshore.")
            print ()
            next_room = 2.11
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "swim" and choice != "back"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "swim" or "back" ? ')
                print ()
                count += 1
                if choice == "swim":
                    if death > 98:
                        print ("As you swim to the middle, you feel something "
                               "touch the bottom of your feet.\nYou hesitate "
                               "but continue swimming. 5 meters away from the "
                               "shore, you feel\nsomething violently grab your"
                               " leg. As you turn your head, you find a demon"
                               "\nmermaid pulling you down, down, down to the "
                               "bottom of the lake. You try to swim to\nthe "
                               "surface for air but the demon mermaid has an "
                               "iron grip on you.\nYou drown in the darkness "
                               "of the lake cavern.")
                        print ()
                        next_room = 100
                    else:
                        print ("You reach the middle and see the treasure "
                               "chest.")
                        print ()
                        next_room = 4.1121
                else:
                    print ("You return to the lakeshore.")
                    print ()
                    next_room = 2.11

    # choice: king (3.21)
    elif next_room == 3.21:
        choice = input('Do you take the quest? "yes" or "no" ? ')
        print ()
        if choice == "yes":
            print ('After you agree, the king tells you, "I seek the Golden '
                   'Apple that is yielded\nby the Tree of Knowledge only once '
                   'every century. The Tree is protected by a\nwise troll. '
                   'Only those that can outwit him may go near the Tree. I '
                   'have a portal\nthat leads straight to the Tree, though '
                   'it may glitch at times, and you\nnever know where you '
                   'may end up. Feel free to choose whatever option you '
                   'want to\nretrieve the fruit."')
            print ()
            next_room = 4.211
        elif choice == "no":
            print ('"Shame..." the king says sadly. He begins to glow and you'
                   'stand still when the\nwizard reveals himself to be the '
                   'king. "I was hoping you would be my\napprentice..." He '
                   'turns slowly, waving his hand in the process. A cloud '
                   'begins\nto warp around you. In a matter of seconds, you '
                   'find yourself back in the\nEnchanted Forest, alone and '
                   'defenseless to the wild creatures of the area.')
            print ()
            next_room = 100
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "yes" and choice != "no"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "yes" or "no" ? ')
                print ()
                count += 1
                if choice == "yes":
                    print ('After you agree, the king tells you, "I seek the '
                           'Golden Apple that is yielded\nby the Tree of '
                           'Knowledge only once every century. The Tree is '
                           'protected by a\nwise troll. Only those that can '
                           'outwit him may go near the Tree. I have a portal'
                           '\nthat leads straight to the Tree, though it may '
                           'glitch at times, and you\nnever know where you may'
                           ' end up. Feel free to choose whatever option you '
                           'want to\nretrieve the fruit."')
                    print ()
                    next_room = 4.211
                else:
                    print ('"Shame..." the king says sadly. He begins to glow '
                           'and you stand still when the\nwizard reveals '
                           'himself to be the king. "I was hoping you would '
                           'be my\napprentice..." He turns slowly, waving his '
                           'hand in the process. A cloud begins\nto warp '
                           'around you. In a matter of seconds, you find '
                           'yourself back in the\nEnchanted Forest, alone and '
                           'defenseless to the wild creatures of the area.')
                    print ()
                    next_room = 100
    # choice: captain (4.1)
    elif next_room == 4.1:
        choice = input('Do you try your luck and "take" the box or "leave" ? ')
        print ()
        if choice == "take":
            if death > 80:
                print ()
                print ("As you reach for the box, your heavy breathing wakes "
                       "the captain. He quickly reaches for his sword and "
                       "quickly slits your throat. Yikes!")
                next_room = 100
            else:
                print ("With your great skill, you take the box without waking"
                       " the captain. You quickly and quietly leave the "
                       "captain's quarters. You open the box and to your "
                       "delight,\nsitting inside the box, wrapped in silk "
                       "is the legendary Acacia wand. All of a\nsudden, two"
                       " vortexes appear in front of you. What do you do?")
                print ()
                next_room = 5.11111
        elif choice == "leave":
            print ("You have returned to the ship deck. What do you want "
                   "to do?")
            print ()
            next_room = 3.111
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "take" and choice != "leave"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "take" or "leave" ? ')
                print ()
                count += 1
                if choice == "take":
                    if death > 80:
                        print ()
                        print ("As you reach for the box, your heavy breathing"
                               " wakes the captain. He quickly reaches for his"
                               " sword and quickly slits your throat. Yikes!")
                        next_room = 100
                    else:
                        print ("With your great skill, you take the box "
                               "without waking the captain. You quickly and "
                               "quietly leave the captain's quarters. You open"
                               " the box and to your delight,\nsitting inside "
                               "the box, wrapped in silk is the legendary "
                               "Acacia wand. All of a\nsudden, two vortexes "
                               "appear in front of you. What do you do?")
                        print ()
                        next_room = 5.11111
                else:
                    print ("You have returned to the ship deck. What do you "
                           "want to do?")
                    print ()
                    next_room = 3.111

    # choice: swim (4.1121)
    elif next_room == 4.1121:
        choice = input('Do you want to try and open the chest? "yes" or '
                       'swim "back" ? ')
        print ()
        if choice == "yes":
            print ("Pirates emerge from the shadows and attack you. You stand "
                   "there shocked as they\ntie you up, gag you, then take "
                   "you to the hanging tree to kill you for trying\nto steal"
                   " their treasure.")
            print ()
            next_room = 100
        elif choice == "back":
            if death > 65:
                print ("As you swim to the middle, you feel something touch "
                       "the bottom of your feet.\nYou hesitate but continue "
                       "swimming. 5 meters away from the shore, you feel"
                       "\nsomething violently grab your leg. As you turn "
                       "your head, you find a demon\nmermaid pulling you "
                       "down, down, down to the bottom of the lake. You try "
                       "to swim to\nthe surface for air but the demon mermaid "
                       "has an iron grip on you.\nYou drown in the darkness of"
                       " the lake cavern.")
                print ()
                next_room = 100
            else:
                print ("You return to the lakeshore.")
                print ()
                next_room = 2.11
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "yes" and choice != "back"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "yes" or "back" ? ')
                print ()
                count += 1
            if choice == "yes":
                print ("Pirates emerge from the shadows and attack you. You "
                       "stand there shocked as they\ntie you up, gag you, "
                       "then take you to the hanging tree to kill you for "
                       "trying\nto steal their treasure.")
                print ()
                next_room = 100
            else:
                if death > 65:
                    print ("As you swim to the middle, you feel something "
                           "touch the bottom of your feet.\nYou hesitate but"
                           " continue swimming. 5 meters away from the shore,"
                           " you feel\nsomething violently grab your leg. As "
                           "you turn your head, you find a demon\nmermaid "
                           "pulling you down, down, down to the bottom of the"
                           " lake. You try to swim to\nthe surface for air but"
                           " the demon mermaid has an iron grip on you.\nYou "
                           "drown in the darkness of the lake cavern.")
                    print ()
                    next_room = 100
                else:
                    print ("You return to the lakeshore.")
                    print ()
                    next_room = 2.11

    # choice: yes apple (4.211)
    elif next_room == 4.211:
        choice = input('Do you risk going through the "portal" or take '
                       'your "pegasus" ? ')
        print ()
        back = random.randint(1, 30)
        if choice == "portal":
            # 30% chance death; 16% chance set back to start given conditions
            if death > 70 and back < 25:
                print ("Disregarding the risk factor, you take a running jump"
                       " toward the portal. In a matter of seconds, you "
                       "realize you're in the middle of shark infested "
                       "waters. You float hopelessly as the man-eating sharks "
                       "approach you curiously. Within five minutes, you're"
                       "torn apart by the sharks, dead.")
                print ()
                next_room = 100
            elif back > 25 and death < 70:
                print ("The portal sent you back to the Enchanted Forest! "
                       "Your pegasus magically appears\nalongside you and "
                       "you are presented with the wizard's initial options.")
                print ()
                next_room = 2
            else:
                print ("The portal has successfully led you to the Tree of "
                       "Knowledge! You walk up the\npath and find a troll "
                       "sitting at the baseof the Tree. Your eyes linger "
                       "towards\nthe shining gold apple a few feet above him "
                       "as you greet him. The troll, being\nwise, knows of "
                       'your intentions. He says, "I will let you take the '
                       'fruit, given\nyou answer this riddle."')
                print ()
                next_room = 5.2111
        elif choice == "pegasus":
            print ("Your instincts tell you to avoid the risk and take the "
                   "safer route. However,\nafter 20 minutes of travel, your "
                   "pegasus begins to falter. He might be hungry.")
            print ()
            next_room = 5.2112
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "portal" and choice != "pegasus"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "portal" or "pegasus" ? ')
                print ()
                count += 1
                if choice == "portal":
                    # 30% chance death; 16% back to start given conditions
                    if death > 70 and back < 25:
                        print ("Disregarding the risk factor, you take a "
                               "running jump toward the portal. In a matter of"
                               " seconds, you realize you're in the middle of "
                               "shark infested waters. You float hopelessly as"
                               "the man-eating sharks approach you curiously. "
                               "Within five minutes, you're torn apart by the "
                               "sharks, dead.")
                        print ()
                        next_room = 100
                    elif back > 25 and death < 70:
                        print ("The portal sent you back to the Enchanted "
                               "Forest! Your pegasus magically appears\n"
                               "alongside you and you are presented with "
                               "the wizard's initial options.")
                        print ()
                        next_room = 2
                    else:
                        print ("The portal has successfully led you to the "
                               "Tree of Knowledge! You walk up the\npath and "
                               "find a troll sitting at the base of the Tree. "
                               "Your eyes linger towards\nthe shining gold "
                               "apple a few feet above him as you greet him. "
                               "The troll, being\nwise, knows of your "
                               'intentions. He says, "I will let you take the '
                               'fruit, given\nyou answer this riddle."')
                        print ()
                        next_room = 5.2111
                else:
                    print ("Your instincts tell you to avoid the risk and take"
                           " the safer route. However,\nafter 20 minutes of "
                           "travel, your pegasus begins to falter. He might be"
                           " hungry.")
                    print ()
                    next_room = 5.2112

    # choice: take (5.11111)
    elif next_room == 5.11111:
        vortex = random.randint(1, 20)
        choice = input('Go to the "left" vortex or the "right" vortex ? ')
        print ()
        if choice == "left" or choice == "right":
            if 1 <= vortex <= 15:
                print ("The vortex takes you to the opening of a cave. You "
                       "feel heat emanating from the\ncave. The vortex has "
                       "disappeared. All you can do is walk to the source of "
                       "heat.\nYou step into the dark cave. As you continue, "
                       "the cave begins to glow red. You\nslowly find yourself"
                       " infront of a chasm. You see a small red rope "
                       "protruding on\nyour right.")
                print ()
                next_room = 6
            else:
                print ("The vortex takes you back to the Enchanted Forest. "
                       "You face the wizard's \ninitial options once again.")
                print ()
                next_room = 2
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "portal" and choice != "pegasus"):
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "portal" or "pegasus" ? ')
                print ()
                count += 1
                if choice == "left" or choice == "right":
                    if 1 <= vortex <= 15:
                        print ("The vortex takes you to the opening of a cave."
                               " You feel heat emanating from the\ncave. The "
                               "vortex has disappeared. All you can do is walk"
                               " to the source of heat.\nYou step into the "
                               "dark cave. As you continue, the cave begins "
                               "to glow red. You\nslowly find yourself infront"
                               " of a chasm. You see a small red rope "
                               "protruding on\nyour right.")
                        print ()
                        next_room = 6
                    else:
                        print ("The vortex takes you back to the Enchanted "
                               "Forest. You face the wizard's\ninitial "
                               "options once again.")
                        print ()
                        next_room = 2

    # choice: tree (5.2111)
    elif next_room == 5.2111:
        print ('"Here is the riddle: What always comes, but never arrives?\n"'
               'You think deeply when finally you come up with an answer')
        print ()
        choice = input('The answer is: ')
        print ()
        if choice.lower() == "tomorrow":
            print ('"Wonderful! You truly do deserve the fruit of the Tree '
                   "of Knowledge!\nHe lets you take the fruit. A vortex "
                   "appears out of nowhere and trust your\ninstincts and "
                   "jump through. You find yourself in the cloud kingdom "
                   "throne room\nonce again and run up to the king and give "
                   "him the golden apple. He graciously\nthanks you and he "
                   "gives you the Acacia wand in return. You walk out "
                   'of the\ncastle, wand in hand. You notice your pegasus '
                   'galloping frantically. You decide\nto get on his back and '
                   'he flies striaght towards an unknown destination.')
            print ()
            next_room = 6.2
        else:
            # kills player if they answer incorrectly
            count = 0
            while count < 4 and (choice != "tomorrow"):
                choice = input('"That is the wrong answer. Here is the riddle '
                               'once again:\n What always comes, but never '
                               'arrives?" You think deeply when finally you '
                               'come up with an answer. "The answer is: ')
                print ()
                count += 1
                if choice.lower() == "tomorrow":
                    print ('"Wonderful! You truly do deserve the fruit of the '
                           'Tree of Knowledge!"\nHe lets you take the fruit. A'
                           ' vortex appears out of nowhere and you trust your'
                           '\ninstincts and jump through. You find yourself'
                           'in the cloud kingdom throne room\nonce again and '
                           'run up to the king and give him the golden apple.'
                           ' He graciously\nthanks you and he gives you the'
                           ' Acacia wand in return. You walk out of the\n'
                           'castle, wand in hand. You notice your pegasus '
                           'galloping frantically. You decide\nto get on his '
                           'back and he flies striaght towards an unknown '
                           'destination.')
                    print ()
                    next_room = 6.2
                    break
                print ('"You have answered incorrectly." The troll slowly '
                       'elongates as he morphs into\nthe wizard. "You have '
                       'failed" he says sadly. He turns, waving his hand. '
                       'A mist\nclouds your sight. You wake up to find '
                       'yourself in the middle of the\nEnchanted Forest '
                       'alone and defenseless to the creatures of the night.')
            print ()
            next_room = 100
    # choice: pegasus (5.2112)
    elif next_room == 5.2112:
        count = 0
        hp = 5
        while count < 4 and hp > 0:
            choice = input('Do you wish to take a "stop" or keep "going" ?')
            print ()
            count += 1
            if choice == "stop":
                print ("You decide to take a break. Your pegasus decends and "
                       "rests for 5 minutes.")
                hp += 0.5
            elif choice == "going":
                print ("Your pegasus is getting tired but keeps going.")
                hp -= 2
            else:
                # kills player if they refuse to answer correctly
                count = 0
                while count < 4 and (choice != "stop" and choice != "going"):
                    choice = input("That wasn't an option. You're testing the "
                                   "wizard's kindness. Choose wisely.\nWhat do"
                                   ' you choose? "stop" or "going" ? ')
                    print ()
                    count += 1
                    if choice == "stop":
                        print ("You decide to take a break. Your pegasus "
                               "decends and rests for 5 minutes.")
                        hp += 0.5
                    else:
                        print ("Your pegasus is getting tired but keeps "
                               "going.")
                        hp -= 2
        if hp <= 0:
            print ("Your pegasus faints. Both of you drop from the sky. "
                   "The pegasus magically\nvanishes as you fall to "
                   "your death.")
            print ()
            next_room = 100
        else:
            next_room = 6.2

    # cave room
    elif next_room == 6:
        choice = input('Do you grab the "rope" or retrace your '
                       'steps "back" ? ')
        print ()
        if choice == "rope":
            print ("As you grab the end of the rope, you realize how scaly "
                   "is it. As you continue to\ntug on the rope, the cave "
                   "begins to rumble. Slowly, two big glowing orbs\nappear"
                   " some feet above you. You realize that you have found "
                   "the Lion Dragon.")
            print ()
            next_room = 7
        elif choice == "back":
            print ('"YOU COWARD!" echoes through the cave. You realize that it'
                   ' is the wizard\nspeaking. The cave continues to rumble, '
                   'and slowly the floor below you begins to\ncrack. There '
                   'is no way of escape. The floor caves in and you fall '
                   'into the lava\nbeds underneath the cave.')
            print ()
            next_room = 100
        else:
            # kills player if they refuse to answer correctly
            count = 0
            while count < 5 and (choice != "rope" and choice != "back"):
                print ()
                choice = input("That wasn't an option. You're testing the "
                               "wizard's kindness. Choose wisely.\nWhat do "
                               'you choose? "rope" or "back" ? ')
                count += 1
                if choice == "rope":
                    print ("As you grab the end of the rope, you realize how "
                           "scaly is it. As you continue to\ntug on the rope, "
                           "the cave begins to rumble. Slowly, two big glowing"
                           " orbs\nappear some feet above you. You realize "
                           "that you have found the Lion Dragon.")
                    print ()
                    next_room = 7
                else:
                    print ('"YOU COWARD!" echoes through the cave. You '
                           "realize that it is the wizard\nspeaking. The "
                           "cave continues to rumble, and slowly the floor "
                           "below you begins to\ncrack. There is no way of "
                           "escape. The floor caves in and you fall "
                           'into the lava\nbeds underneath the cave.')
                    print ()
                    next_room = 100

    # choice: tomorrow (6.2); redirects to different room; blank room
    elif next_room == 6.2:
        print ("The pegasus finally lands on a deserted island. A cave lurks "
               "ahead. You feel\nheat emanating from the cave. The pegasus "
               "has disappeared. All you can do is\nwalk to the source of "
               "heat. You step into the dark cave. As you continue, the\ncave"
               " begins to glow red. You slowly find yourself infront of a "
               "chasm. You see a\nsmall red rope protruding on your right.")
        print ()
        next_room = 6

    # final room
    elif next_room == 7:
        print ("You pull out your wand as quickly as you can and face the "
               "dragon.")
        print ()
        hp = 20
        dragon = random.randint(1, 10)
        count = 0
        while count < 4 and hp > 0:
            print ('Do you wish to cast a damage spell?')
            choice = input('"yes" or "no"? ')
            print()
            count += 1
            if choice == "yes":
                if dragon > 9:
                    print ("The dragon dodged your spell and attacked you in "
                           "retaliation.")
                    print ()
                    hp -= 4
                else:
                    print ("Your spell effectively damaged the dragon.")
                    print ()
            elif choice == "no":
                print ("The dragon is upset and attacked you.")
                print ()
                hp -= 8
            else:
                # kills player if they refuse to answer correctly
                count = 0
                while count < 4 and (choice != "yes" and choice != "no"):
                    print ()
                    choice = input("That wasn't an option. You're testing the "
                                   "wizard's kindness. Choose wisely.\nWhat do"
                                   ' you choose? "yes" or "no" ? ')
                    print ()
                    count += 1
                    if choice == "yes":
                        if dragon > 9:
                            print ("The dragon dodged your spell and attacked "
                                   "you in retaliation.\nDo you wish to cast"
                                   " a damage spell?")
                            print ()
                            hp -= 4
                        else:
                            print ("Your spell effectively damaged the dragon."
                                   "\nDo you wish to cast another spell?")
                            print ()
                    else:
                        print ("The dragon is upset and attacked you.\nDo you "
                               "wish to cast a damage spell?")
                        print ()
                        hp -= 8
        if hp <= 0:
            print ("You died trying to defeat the Lion Dragon. As you "
                   "distentegrate, the Acacia wand\nstays intact. The wand"
                   " falls to the cave floor. It's sound echoing throughout"
                   "\nas your ashes are carried by a passing breeze.")
            print()
            next_room = 100
        else:
            print ("The dragon begins to glow. It glows brighter and brighter"
                   " as it shrinks. The\nglowing object becomes a princess. "
                   "The wizard apparates out of thin air and\nthanks you "
                   "greatly for saving his daughter. He welcomes you as his "
                   "apprentice\nand takes you under his wing.")
            print ()
            print ("YOU WIN!!!")
            next_room = 0

    # death suite
    if next_room == 100:
        print ("You are not worthy to serve the wizard.")
        choice = input('Do you want to try again? "yes" or "no" ?')
        print ()
        if choice == "yes":
            next_room = 1
        else:
            next_room = 0

print ("Game Over.")
