import pygame

# Set up game window
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pong")

# Set up game objects
player1 = pygame.Rect(50, 200, 20, 100)
player2 = pygame.Rect(570, 200, 20, 100)
ball = pygame.Rect(320, 240, 20, 20)
ball_speed = [5, 5]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move_ip(0, -5)
    if keys[pygame.K_s]:
        player1.move_ip(0, 5)
    if keys[pygame.K_UP]:
        player2.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player2.move_ip(0, 5)

    # Move ball
    ball.move_ip(ball_speed)
    if ball.top < 0 or ball.bottom > 480:
        ball_speed[1] = -ball_speed[1]
    if ball.left < player1.right and player1.top < ball.centery < player1.bottom:
        ball_speed[0] = -ball_speed[0]
    if ball.right > player2.left and player2.top < ball.centery < player2.bottom:
        ball_speed[0] = -ball_speed[0]
    if ball.left < 0 or ball.right > 640:
        ball_speed = [1, 1]

    # Draw game objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player1)
    pygame.draw.rect(screen, (255, 255, 255), player2)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.display.update()
