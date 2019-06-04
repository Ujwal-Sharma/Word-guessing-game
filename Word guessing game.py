from random import randint

words = ["apple","kiwi","human","light","laptop","jupiter","notebook","phone","smartphone","kangaroo"] # A list with words
words_hints = ["a red fruit","a fruit with the name of a bird","the smartest species in the world","which has a speed of 3 x 10^8","portable computer","a gas giant full of hydrogen and helium","something used to write on","a communication device used for making calls","a smart communication device used for making calls and doing smart stuff","found in Australia(can punch the shit out of u"] # A list with hints of the words in the corresponding position

the_word_pos = randint(0,len(words)-1) # Choose a random position for random word
the_word = words[the_word_pos] # The word chosen randomly
the_word_hint = words_hints[the_word_pos] # Hint for the word
the_word_guess = the_word # Initialize the word used to display

no_of_blank = round(len(the_word) / 2 + 0.1) # no_of_blank is initialized to half of the length of the word rounded up
max_wrong_guesses = no_of_blank # max_wrong_guessess is initianized to no_of_blank

i = no_of_blank # Initialize iterator i to no_of_blank
blank_ = []

while i > 0: # Loop through the iterator (which is just no_of_blank)
    pos_blank = randint(0,len(the_word)-1) # Choose a random position in the word to make it blank
    if not(pos_blank in blank_): # If the letter in pos_blank is not already blank
        blank_+=[pos_blank]+[the_word[pos_blank]] # Store pos_blank and the letter at pos_blank in blank_
        the_word_guess = the_word_guess[:pos_blank] + "_" + the_word_guess[pos_blank+1:] # Replace the letter in pos_blank as an underscore
        i -= 1 # iterator - 1

no_of_wrong_guesses = 0 # Initialize no_of_wrong_guesses
print("Guess the letters in the blanks of the given word one by one")
while no_of_blank > 0 and no_of_wrong_guesses < max_wrong_guesses:
    print("U can guess")
    x = input(the_word_guess + "\n")
    if x in blank_: # If x is in the list storing the letters replaced and their positions
        print("That is correct")
        pos_blank=blank_[blank_.index(x)-1] # position of the blank which was guessed correctly
        the_word_guess = the_word_guess[:pos_blank] + the_word[pos_blank] + the_word_guess[pos_blank+1:] # Replacing the underscore with the letter which was guessed correctly to the word being displayed
        no_of_blank -= 1 # no_of_blanks in the_word_guess was reduced by one
        blank_.remove(pos_blank) # remove pos_blank from blank_ since that blank is filled
        blank_.remove(x) # remove x from blank_ since that blank is filled
    else:
        print("That is wrong")
        no_of_wrong_guesses += 1
        if no_of_wrong_guesses == max_wrong_guesses - 1: # If there is only one chance left for the user
            print("You are not doing so good, so here's a hint for the word:"+"\n"+the_word_hint)
        
if no_of_blank == 0: # If there are no blanks left after filling
    print("U won! The word is",the_word)
    
else: # If there is at least a blank left after filling
    print("Uh oh, u lost, the word is",the_word)
