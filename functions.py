#recieve input of word to be used
#prompt user for letter, check letter and respond appropriately
import pygame


def get_word():
    letterCap = 20
    
    word = input("What is your chosen word?\n").upper() #gets word, converts all to uppercase
    
    try:#checks if all characters are letters, and if fits letter cap
        if not word.isalpha(): 
            raise ValueError("Invalid Word. No special characters, spaces or numbers.")
        
        if len(word) > letterCap:
            raise ValueError("Max letter cap of 10 reached.")
            
        letters = list(word)
        spaces = []
        
        for i in range(len(letters)):
            spaces.append('_')
        
        #testings
        # print(letters)
        # print(spaces)
    
    except ValueError as e:
        print("Error:", e)
        
    return letters, spaces
    
    
def check_letter(letters, spaces, wrongs):
    guess = input("Enter a letter to guess. \n").upper()
    
    try: #checks if inputted exactly 1 letter to guess
        if len(guess) > 1:
            raise ValueError("Only guess one letter at a time")
        
        elif len(guess) < 1:
            raise ValueError("Guess a letter")
    
    except ValueError as e:
        print("Error:", e)
    
    correctGuess = False
    for i in range(len(letters)): #change all correctly guessed letters
        if letters[i] == guess:
            spaces[i] = guess
            correctGuess = True
    
    if correctGuess:
        print("Correct guess!!!")
    
    if not correctGuess:
        print("Incorrect guess...")
        wrongs.append(guess) #append guess to 'wrongs' array
        
        
    #checks if games still running
    gameRunning = False
    for i in range(len(letters)):
        if spaces[i] == '_':
            gameRunning = True
        
    #testings    
    # print(letters)
    # print(spaces)
    # print(wrongs)
    
    return letters, spaces, wrongs, gameRunning
        

#testing
# testletters, testspaces = get_word()
# testwrongs = []
# testletters, testspaces, testwrongs, testgameRunning = check_letter(testletters, testspaces, testwrongs)

# if testgameRunning == True:
#     print("game is running")
    
# elif testgameRunning == False:
#     print("game is NOT running")
#testing




# draws the hangman based on number of wrong guesses (0-6)
def drawHangman(screen, wrong_guesses):
    # constants for positioning
    base_x = 200
    base_y = 400
    pole_height = 250
    
    # draw hanger
    pygame.draw.line(screen, (0,0,0), (base_x, base_y), (base_x + 150, base_y), 10)  # base
    pygame.draw.line(screen, (0,0,0), (base_x + 50, base_y), (base_x + 50, base_y - pole_height), 10)  # vertical pole
    pygame.draw.line(screen, (0,0,0), (base_x + 50, base_y - pole_height), (base_x + 150, base_y - pole_height), 10)  # horizontal beam
    pygame.draw.line(screen, (0,0,0), (base_x + 150, base_y - pole_height), (base_x + 150, base_y - pole_height + 50), 10)  # rope

    # draw body parts
    head_center = (base_x + 150, base_y - pole_height + 75)
    body_start = (base_x + 150, base_y - pole_height + 100)
    body_end = (base_x + 150, base_y - pole_height + 160)
    
    if wrong_guesses >= 1:  # head
        pygame.draw.circle(screen, (0,0,0), head_center, 25, 3)
    
    if wrong_guesses >= 2:  # body
        pygame.draw.line(screen, (0,0,0), body_start, body_end, 3)
    
    if wrong_guesses >= 3:  # left arm
        pygame.draw.line(screen, (0,0,0), 
                        (base_x + 150, base_y - pole_height + 110),
                        (base_x + 120, base_y - pole_height + 140), 3)
    
    if wrong_guesses >= 4:  # right arm
        pygame.draw.line(screen, (0,0,0),
                        (base_x + 150, base_y - pole_height + 110),
                        (base_x + 180, base_y - pole_height + 140), 3)
    
    if wrong_guesses >= 5:  # left leg
        pygame.draw.line(screen, (0,0,0),
                        body_end,
                        (base_x + 120, base_y - pole_height + 200), 3)
    
    if wrong_guesses >= 6:  # right leg
        pygame.draw.line(screen, (0,0,0),
                        body_end,
                        (base_x + 180, base_y - pole_height + 200), 3)