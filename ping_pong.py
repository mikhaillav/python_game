import pygame

pygame.init()
pygame.font.init()           

game_over = 0
game_over2 = 0

width_win = 1000
heigth_win = 600

players_width = 10
players_height = 170

d_players = 50

player1_x = width_win - d_players
player1_y = heigth_win / 2 - players_height / 2 - 100

player_x = d_players
player_y = heigth_win / 2 - players_height / 2
players_color = (255, 255, 255)

ball_x = width_win / 2
ball_y = heigth_win / 2
ball_rad = 17
ball_color = (255, 255, 255)

speed = 10

vector_x = 1
vector_y = 1
                         
win = pygame.display.set_mode((width_win, heigth_win))

pygame.display.set_caption("pong")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    f1 = pygame.font.Font(None, 50)
    score1 = f1.render(str(game_over2), False,players_color)
    f2 = pygame.font.Font(None, 50)
    score2 = f2.render(str(game_over), False,players_color)

    win.blit(score1, (400, 30))
    win.blit(score2,(600,30))

    if game_over2 == 5:
        pygame.quit()

    if game_over == 5:
        pygame.quit()

    pygame.time.delay(20)

    pygame.draw.rect(win, (players_color), (player_x, player_y, players_width, players_height))
    pygame.draw.rect(win, (players_color), (player1_x,player1_y, players_width, players_height))
    
    pygame.draw.rect(win, (255,255,255), (width_win/2,0, 10, 700))
    
    pygame.draw.circle(win, (ball_color), (ball_x, ball_y), ball_rad)

    pygame.display.update()

    win.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and  player_y > 15:
        player_y = player_y - speed
    elif keys[pygame.K_s] and player_y < 600 - players_height - 15:
        player_y = player_y + speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player1_y > 15:
        player1_y = player1_y - speed
    elif keys[pygame.K_DOWN] and player1_y < 600 - players_height - 15:
        player1_y = player1_y + speed    

    if ball_x <= player_x and ball_y >= player_y and ball_y <= player_y + players_height:
        vector_x = -vector_x

    if ball_x >= player1_x and ball_y >= player1_y and ball_y <= player1_y + players_height:
        vector_x = -vector_x  

    if ball_y <= 0 or ball_y >= heigth_win:
        vector_y = -vector_y
        
    ball_x -= speed * vector_x
    ball_y -= speed * vector_y

    if ball_x <= 0:
        game_over += 1
        ball_x = width_win / 2
        ball_y = heigth_win / 2
        ball_x -= speed * vector_x
        ball_y -= speed * vector_y

    if ball_x >= width_win:
        game_over2 += 1
        ball_x = width_win / 2
        ball_y = heigth_win / 2
        ball_x += speed * vector_x
        ball_y += speed * vector_y