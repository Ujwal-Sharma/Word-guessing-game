from random import randint

words = ["apple","kiwi","human","light","laptop","jupiter","notebook","phone","smartphone","kangaroo"]
words_hints = ["a red fruit","a fruit with the name of a bird","the smartest species in the world","which has a speed of 3 x 10^8","portable computer","a gas giant full of hydrogen and helium","something used to write on","a communication device used for making calls","a smart communication device used for making calls and doing smart stuff","found in Australia(can punch the shit out of u"]

the_word_pos = randint(0,len(words)-1)
the_word = words[the_word_pos]
the_word_hint = words_hints[the_word_pos]
the_word_guess = the_word

no_of_blank = round(len(the_word) / 2 + 0.1)
max_wrong_guesses = no_of_blank

i = no_of_blank
ad_blank = {}

while i > 0:
    pos_blank = randint(0,len(the_word)-1)
    if not(pos_blank in ad_blank.values()):
        ad_blank[the_word[pos_blank]] = pos_blank
        the_word_guess = the_word_guess[:pos_blank] + "_" + the_word_guess[pos_blank+1:]
        i -= 1

no_of_wrong_guesses = 0
print("Guess the letters in the blanks of the given word one by one")
while no_of_blank > 0 and no_of_wrong_guesses < max_wrong_guesses:
    print("U can guess")
    x = input(the_word_guess + "\n")
    if x in ad_blank:
        print("That is correct")
        the_word_guess = the_word_guess[:ad_blank[x]] + the_word[ad_blank[x]] + the_word_guess[ad_blank[x]+1:]
        no_of_blank -= 1
    else:
        print("That is wrong")
        no_of_wrong_guesses += 1
        if no_of_wrong_guesses == max_wrong_guesses - 1:
            print("You are not doing so good, so here's a hint for the word:")
            print(the_word_hint)
        
if no_of_blank == 0:
    print("U won! the word is",the_word)
    
else:
    print("Uh oh, u lost, the word is",the_word)