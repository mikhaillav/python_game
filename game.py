import pygame

pygame.init()

width_win = 1000
heigth_win = 600

player_width = 10
player_height = 200

player_x = 10
player_y = heigth_win / 2 - player_height / 2
player_color = (173, 255, 47)

ball_x = width_win / 2
ball_y = heigth_win / 2
ball_rad = 20
ball_color = (255, 255, 0)

speed = 10

vector_x = 1
vector_y = 1

win = pygame.display.set_mode((width_win, heigth_win))

pygame.display.set_caption("game")

while True:
    
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(win, (player_color), (player_x, player_y, player_width, player_height))

    # pygame.draw.rect(win, (255,255,255), (x1,y1, 10, 200))
    pygame.draw.rect(win, (255,255,255), ( 500,0, 10, 700))
    
    pygame.draw.circle(win, (ball_color), (ball_x, ball_y), ball_rad)

    pygame.display.update()

    win.fill((0,0,0))

    ball_x -= speed * vector_x
    ball_y -= speed * vector_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y = player_y + speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player_y = player_y - speed

    if ball_x <= 10 and ball_y > (player_y - player_height):
        vector_x = -vector_x    

    if ball_x >= width_win or ball_x <= 0:
        pygame.quit()

    if ball_y >= heigth_win or ball_y <= 0:
        vector_y = -vector_y
