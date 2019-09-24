

# Python Counting Game =================================================================================================

# Introduction for the user. -------------------------------------------------------------------------------------------
print("Welcome to The Number Game!")
print("In this game, there is a counter that starts at 0. The game will end when the counter reaches or passes 100.")
print("You will first pick an integer between 1 and 10 which will be added to the counter.")
print("Your opponent will then pick an integer from 1 to 10 and then his pick will be added to the counter as well.")
print("This cycle will continue until the counter reaches or passes 100.")
print("Whoever's turn it is when that happens is the winner of the game!")
print(" ")
print("Good Luck")
print(" ")

# The initial value for the counter is set. ----------------------------------------------------------------------------
tally = 0
print("The current tally is: 0")

# In this while loop is the main game. The game will continue to go on as long as the counter is less than 100. --------
while tally < 100:

# This is the loop for Player 1's input. It will only accept an integer from 1 to 10 and will add it to the counter. ---
    player_1_in = int(input("Enter an integer from 1 to 10: "))
    if 1 <= player_1_in <= 10:
        tally += player_1_in                        # Counter + Player 1's pick.
        print("The current tally is: ", tally)
    else:                                           # If Player 1 did not pick an integer from 1 to 10 the game will...
        while 1 > player_1_in or 10 < player_1_in:                  # ... ask a second time. ---------------------------
            player_1_in = int(input("Your integer needs to be from 1 to 10. Choose again: "))
        else:
            tally += player_1_in
            print("The current tally is: ", tally)
    if tally >= 100:
        print("You Have Won!")                     # Because this if-else loop is at the end of Player 1's process...
    else:                                                       # ... Player 1 will be the winner if 100 is reached. ---
        import random                               # For Player 2 the computer picks a random integer from 1 to 10. ---
        for x in range(1):
            player_2_in = random.randint(1, 10)
            tally += player_2_in                    # That random integer is then added to the counter. ----------------
            print("Your opponent has chosen: ", player_2_in)
            print("The current tally is: ", tally)
        if tally >= 100:                            # Player 2 is declared the winner if Player 1 did not reach 100 yet.
            print("Your Opponent Has Won!")

# End of Program =======================================================================================================

