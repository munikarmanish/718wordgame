# This file implements the word_game.
# Helper modules are in word_module.py

# YOUR NAME HERE PLEASE

import word_module as wm

# Playing a game is done in the following steps:

# YOU HAVE TO DO THIS according to the following
# specification.

"""
Allow the user to play a series of hands

* Asks the user to input a total number of hands

* Accumulates the score for each hand into a total score for the
  entire series

* BONUS TASK:
  For each hand, before playing, ask the user if they want to substitute
  one letter for another. If the user inputs 'yes', prompt them for their
  desired letter. This can only be done once during the game. Once the
  substitue option is used, the user should not be asked if they want to
  substitute letters in the future.

* BONUS TASK:
  For each hand, ask the user if they would like to replay the hand.
  If the user inputs 'yes', they will replay the hand and keep
  the better of the two scores for that hand.  This can only be done once
  during the game. Once the replay option is used, the user should not
  be asked if they want to replay future hands. Replaying the hand does
  not count as one of the total number of hands the user initially
  wanted to play.

* Note: if you replay a hand, you do not get the option to substitute
        a letter - you must play whatever hand you just had.

* prints the total score for the series of hands and finished the program

"""

# print welcome message and get going
print("Welcome to the physics718 word game!")
print("====================================")
print()

# load word list:
word_list = wm.load_words()

hand_size = 10 # size of a hand; you can change this if yu want to!

print("Now we can start!")

# Get number of hands to play
num_hands = 0
while num_hands < 1:
    try:
        num_hands = int(input("How many hands do you want to play? "))
    except ValueError:
        pass
  
total_score = 0
substitution_used = False
replay_used = False

for i in range(num_hands):
    hand = wm.deal_hand(hand_size)
    print("New hand: ")
    wm.display_hand(hand)

    if not substitution_used:
        substitute = input('Do you want to substitute a letter? (yes/no) ')
        if substitute.lower() == 'yes':
            substitution_used = True
            letter = input('Which letter do you want to subsitute? ')
            hand = wm.substitute_hand(hand, letter)
            print("New hand: ")
            wm.display_hand(hand)

    hand_score = wm.play_hand(hand, word_list)

    if not replay_used:
        replay = input('Do you want to replay hand? (yes/no) ')
        if replay.lower() == 'yes':
            replay_used = True
            hand_score_replay = wm.play_hand(hand, word_list)
            hand_score = max(hand_score, hand_score_replay)

    total_score += hand_score

# Print final score
print("Total score over {num_hands} hands: {total_score}".format(
    num_hands=num_hands,
    total_score=total_score
))
print("Game over!")