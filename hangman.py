import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running =  True

# initialise font and word
font = pygame.font.Font(None, 48)  # None = default font, 48 = size
word = "HELLO PYGAME"

#initialise GUI
screen.fill((255,255,255)) # add logic instead here 
pygame.draw.rect(screen, (0,0,0), (300,360,200,100),10) # example rectangle


#add functions 






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255)) # add logic instead here 
    pygame.draw.rect(screen, (0,0,0), (300,360,200,100),10) # example rectangle
    
    text_surf = font.render(word, True, (0,0,0))   # (text, antialias, color)
    text_rect = text_surf.get_rect(center=(640, 80))  # position: center x=640, y=80
    screen.blit(text_surf, text_rect)
    
    pygame.display.flip()   #refresh on-screen display
    clock.tick(60)          # next frame 60 FPS    
