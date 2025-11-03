import pygame
import pygame_gui
import functions

pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running =  True

# initialise font and word
font = pygame.font.Font(None, 48)  # None = default font, 48 = size
word = "HANG MAN GAME"

#initialise GUI
pygame.display.set_caption('Hangman Game')
manager = pygame_gui.UIManager((1000, 1000))

screen.fill((255,255,255)) # add logic instead here 

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 800), (150, 50)),text='Gay-meh Starto',manager=manager)


#add functions 




while running:
    time_delta = clock.tick(60) / 1000.0 # seconds since last frame
    
    for event in pygame.event.get():
        manager.process_events(event)  
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print("Hello World!")
                pygame.draw.rect(screen, (0,0,0), (100, 100, 800, 600), 10)
                text_surf = font.render(word, True, (0,0,0))
                text_rect = text_surf.get_rect(center=(500, 80))
                screen.blit(text_surf, text_rect)
                functions.drawHangman(screen, 3)  
                
    manager.update(time_delta)   

    
    # screen.fill((255, 255, 255))


    manager.draw_ui(screen)                              # draw GUI elements (buttons, etc.)

    pygame.display.update()