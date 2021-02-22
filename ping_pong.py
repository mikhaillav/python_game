import pygame

pygame.init()

width_win = 1000
heigth_win = 600

players_width = 10
players_height = 200

d_players = 50

player1_x = width_win - d_players
player1_y = heigth_win / 2 - players_height / 2 - 100

player_x = d_players
player_y = heigth_win / 2 - players_height / 2
players_color = (255, 255, 255)

ball_x = width_win / 2
ball_y = heigth_win / 2
ball_rad = 20
ball_color = (255, 255, 255)

speed = 10

vector_x = 1
vector_y = 1

win = pygame.display.set_mode((width_win, heigth_win))

pygame.display.set_caption("game")

while True:
    
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(win, (players_color), (player_x, player_y, players_width, players_height))
    pygame.draw.rect(win, (players_color), (player1_x,player1_y, players_width, players_height))
    
    pygame.draw.rect(win, (255,255,255), ( 500,0, 10, 700))
    
    pygame.draw.circle(win, (ball_color), (ball_x, ball_y), ball_rad)

    pygame.display.update()

    win.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player_y = player_y + speed
    elif keys[pygame.K_w]:
        player_y = player_y - speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1_y = player1_y - speed
    elif keys[pygame.K_DOWN]:
        player1_y = player1_y + speed    

    if ball_x <= player_x and ball_y >= player_y and ball_y <= player_y + players_height:
        vector_x = -vector_x

    if ball_x >= player1_x and ball_y >= player1_y and ball_y <= player1_y + players_height:
        vector_x = -vector_x  

    if ball_y <= 0 or ball_y >= heigth_win:
        vector_y = -vector_y
        
    ball_x -= speed * vector_x
    ball_y -= speed * vector_y

    if ball_x <= 0 or ball_x >= width_win:
        pygame.quit()