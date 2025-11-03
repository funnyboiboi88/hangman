import pygame 
import pygame_gui
import functions

# initialise GUI window
pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running =  True
game_stage = 0
screen.fill((255,255,255)) 
pygame.display.set_caption('Hangman Game')
manager = pygame_gui.UIManager((1000, 1000), theme_path='theme.json')
chosen_word = ''

letters = []
spaces = []
wrongs = []

# initialise font and word
font = pygame.font.Font(None, 48)  # None = default font, 48 = size
word = "HANG MAN GAME"

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 450), (150, 50)),text='Gay-meh Starto',manager=manager)
word_chooser_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 550), (150, 50)),text = 'Submit Word', manager=manager) 
word_chooser_button.hide()   


while running:
    time_delta = clock.tick(60) / 1000.0 # seconds since last frame
    screen.fill((255,255,255))  #frame clearer

        
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
                
        if event.type == pygame.KEYDOWN:
            if game_stage == 1:
                if event.key == pygame.K_BACKSPACE:
                    chosen_word = chosen_word[:-1]
                else:
                    ch = event.unicode  
                    if ch and ch.isalpha():   # only letters 
                        chosen_word += ch.upper()




    if game_stage == 1:
        pygame.draw.rect(screen, (0,0,0), (100, 100, 800, 600), 10)
        functions.display_word(screen, word, (0,0,0), (500, 80),font)
        functions.display_word(screen, "what is your chosen word?", (0,0,0), (500, 250),font)
        
        word_chooser_button.show()
        functions.display_word(screen, chosen_word, (0,0,0), (500, 500),font)
        
    elif game_stage == 2:
        pygame.draw.rect(screen, (0,0,0), (100, 100, 800, 600), 10)
        functions.display_word(screen, word, (0,0,0), (500, 80),font)
        functions.draw_hangman(screen, 0)  # example: draw hangman with 2 wrong guesses
        functions.display_word(screen, '      '.join(spaces), (0,0,0), (500, 600),font)

    manager.draw_ui(screen)        # draw GUI elements (buttons, etc.)
    manager.update(time_delta)   
    pygame.display.update()