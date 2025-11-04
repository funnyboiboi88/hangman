import pygame 
import pygame_gui
import functions

# initialise GUI window
pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
screen.fill((255,255,255)) 
pygame.display.set_caption('Hangman Game')
manager = pygame_gui.UIManager((1000, 1000), theme_path='theme.json')

running =  True
game_stage = 0
chosen_word = ''
chosen_letter = ''
letters = []
spaces = []
wrongs = []
game_won = False

# initialise font and word
font = pygame.font.Font(None, 48)  # None = default font, 48 = size
word = "HANG MAN GAME"

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 450), (150, 50)),text='Gay-meh Starto',manager=manager)
word_chooser_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 550), (150, 50)),text = 'Submit Word', manager=manager) 
word_chooser_button.hide()   
letter_chooser_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 475), (150, 50)),text = 'Submit Letter', manager=manager)
letter_chooser_button.hide()
restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 900), (150, 50)),text = 'Restart', manager=manager)
restart_button.hide()
play_again_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 475), (150, 50)),text = 'Play Again', manager=manager)
play_again_button.hide()


while running:
    time_delta = clock.tick(60) / 1000.0 # seconds since last frame
    screen.fill((255,255,255))  #frame clearer
    
    # functions.display_word(screen, 'game stage: ' + str(game_stage) + '\nlives: '+str(6-len(wrongs)), (0,0,0), (200, 900),font)
    

        
    for event in pygame.event.get():
        manager.process_events(event)  
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED: 
            if event.ui_element == start_button:
                print("Game has started!")
                
                game_stage = 1
                start_button.hide()
            if event.ui_element == word_chooser_button:
                letters, spaces, valid_word = functions.get_word(chosen_word)
                if valid_word:
                    word_chooser_button.hide()
                    game_stage = 2  
            if event.ui_element == letter_chooser_button:
                letters, spaces, wrongs, game_won = functions.check_letter(letters, spaces, wrongs, chosen_letter)
                chosen_letter = ''  # reset chosen letter after submission
            if event.ui_element == restart_button or event.ui_element == play_again_button:
                game_stage = 1
                chosen_word = ''
                chosen_letter = ''
                letters = []
                spaces = []
                wrongs = []
                game_won = False
                
        if event.type == pygame.KEYDOWN:
            if game_stage == 1:
                if event.key == pygame.K_BACKSPACE:
                    chosen_word = chosen_word[:-1]
                else:
                    ch = event.unicode  
                    if ch and ch.isalpha():   # only letters 
                        chosen_word += ch.upper()
                        
            if game_stage == 2:
                if event.key == pygame.K_BACKSPACE:
                    chosen_letter = chosen_letter[:-1]
                else:
                    ch = event.unicode  
                    if ch and ch.isalpha() and len(chosen_letter)<1:   # only letters 
                        chosen_letter += ch.upper()



    if game_stage == 0:
        functions.display_word(screen, 'Welcome to Hangman! \ncreated by : DL JO ML', (0,0,0), (500, 200),font)

    
    if game_stage == 1:
        pygame.draw.rect(screen, (0,0,0), (100, 100, 800, 600), 10)
        functions.display_word(screen, word, (0,0,0), (500, 80),font)
        functions.display_word(screen, "what is your chosen word?", (0,0,0), (500, 250),font)
        letter_chooser_button.hide()
        restart_button.hide()
        play_again_button.hide()
        word_chooser_button.show()
        functions.display_word(screen, chosen_word, (0,0,0), (500, 500),font)
        
    elif game_stage == 2:
        pygame.draw.rect(screen, (0,0,0), (100, 100, 800, 600), 10)
        functions.display_word(screen, word, (0,0,0), (500, 80),font)
        functions.draw_hangman(screen, len(wrongs))  
        functions.display_word(screen, '      '.join(spaces), (0,0,0), (500, 600),font)
        functions.display_word(screen, 'Guess a Letter!!', (0,0,0), (500, 400),font)
        functions.display_word(screen, chosen_letter, (0,0,0), (500, 500),font)
        letter_chooser_button.show()
        restart_button.show()
        functions.display_word(screen, 'Wrong Letters: ' +' '.join(wrongs), (0,0,0), (500, 750),font)
        functions.display_word(screen,'lives: '+str(6-len(wrongs)), (0,0,0), (200, 900),font)
        
        if game_won == True or len(wrongs) == 6:
            game_stage = 3  # player has won or lost
            
    elif game_stage == 3:
        letter_chooser_button.hide()
        restart_button.hide()
        
        if game_won == True:
            functions.display_word(screen, 'You Win!!', (50,255,50), (500, 400),font)
            play_again_button.show()
        else:
            functions.display_word(screen, 'You Lose!! The word was: ' + ''.join(letters), (255,0,0), (500, 400),font)
            play_again_button.show()

        

    manager.draw_ui(screen)        # draw GUI elements (buttons, etc.)
    manager.update(time_delta)   
    pygame.display.update()