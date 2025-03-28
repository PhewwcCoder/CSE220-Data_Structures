import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

running = True
x, y = 400, 300  # Player position

while running:
    screen.fill((0, 0, 0))  # Clear screen (black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 2
    if keys[pygame.K_RIGHT]: x += 2
    if keys[pygame.K_UP]: y -= 2
    if keys[pygame.K_DOWN]: y += 2
    
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))  # Draw player
    pygame.display.update()  # Update screen

pygame.quit()