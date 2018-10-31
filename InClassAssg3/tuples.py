# import random and permutations
import random
from itertools import permutations

game = True

print ('You have three chances to get the word right; otherwise u die.')
print ()
# 20 word tuple
tuples = ('witch', 'smoke', 'snake', 'scary', 'haunted', 'candy', 'costume',
          'slime', 'spooky', 'treat', 'trick', 'black', 'cauldron', 'spider',
          'mummy', 'cobweb', 'ghost', 'zombie', 'wizard', 'pumpkin')
score = 0
while game:
    # chooses a random word from tuple
    word = random.choice(tuples)

    # creates permutations of the word chosen
    perm = [''.join(p) for p in permutations(word)]

    # chooses one permutation from generated words
    perm1 = random.choice(perm)
    print (perm1)
    print ()

    # while loop to stop at 3 guesses
    count = 0
    while count < 3:
        guess = input("What's the word? ")
        print()
        if guess == word:
            print ("ur not stupid")
            print ()
            score += 1
            break
        else:
            print("ur stupid")
            print ()
            count += 1
    print ("ur score is: ", score)
    print ()
    choice = input("want a new word (press any key) or quit (q)? ")
    print ()
    if choice == 'q':
        print ('tf. k.')
        print()
        break

print ("ur final score is ", score)
