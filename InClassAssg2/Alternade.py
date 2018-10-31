# alternades

# boolean for while loop
human = True

# while statement to keep program going until word is formed
while human:
    choice = input("Do you want to construct (c) or destruct (d) ?")
    print ()
    # destruct if statement
    if choice == "d":
        word = input("Enter a word: ")
        # index operators with step 2
        word1 = word[::2]
        print (word1)
        # index operators starting at 1 with step 2
        word2 = word[1::2]
        print (word2)
        human = False
    # construct elif statement
    elif choice == 'c':
        word1 = input("Enter word 1: ")
        word2 = input("word 2: ")
        # variable for count and number of letters
        x = 0
        newword = ''
        # while loop to generate new word
        # will only stop when x exceeds number of letters for both words
        while x < len(word1) and x < len(word2):
            newword += word1[x] + word2[x]
            x += 1
        print (newword)
        human = False
    else:
        print ("Invalid input")
        print ()
