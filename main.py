import pygame
import time
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('kolikoregular', 30)
scoreFont = pygame.font.SysFont('kolikoregular', 20)
print(pygame.font.get_fonts())

width = 800
height = 600
window = pygame.display.set_mode((width, height))
score = 0
highScore = 0

#colours
offwhite = (249, 246, 244)
offblack= (35, 35, 34)

#ball movement (variables)
xCount = 400
yCount = 10
direction = 1
directionY = 1
paddleX = 400
frame = 0

#score counter
waitTicks = 0
touched = False


#main loop
while True:
    frame += 1
    keys = pygame.key.get_pressed()
    if xCount % 2 == 0:
        if keys[pygame.K_LEFT]:
            paddleX -= 1
        elif keys[pygame.K_RIGHT]:
            paddleX += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #display
    window.fill(offwhite)
    #paddle collision
    paddleRect = pygame.Rect(paddleX, 500, 95, 40)
    ballRect = pygame.Rect(xCount, yCount, 20, 20)
    #ball movement (counter)
    if frame % 2 == 0:
        xCount += direction
        yCount += directionY
    #if not touching paddle, normal movement
    if xCount >= width:
        direction = -1
    elif xCount <= 0:
        direction = 1
    #game over if it hits the bottom part of the frame
    if yCount >= height:
        gameoverText = font.render('game over..', False, offblack)
        window.blit(gameoverText, (350, 100))
        if score > highScore:
            highScoreText = font.render('new high score!', False, offblack)
            window.blit(highScoreText, (350, 150))
            highScore = score
        score = 0
        xCount, yCount, direction = 400, 50, 1
        time.sleep(3)
    elif yCount <= 0:
        directionY = 1
    #collide thing
    if touched == True:
        waitTicks += 1
    if waitTicks >= 150:
        touched = False
        waitTicks = 0
    if paddleRect.colliderect(ballRect):
        directionY = -1
        if touched == False:
            score += 1
            touched = True
    #score stuff
    scoreText = scoreFont.render('score: ' + str(score), False, offblack)
    highScoreText = scoreFont.render('high score: ' + str(highScore), False, offblack)
    #rendering
    pygame.draw.circle(window, offblack, (xCount, yCount), 20, 3)
    pygame.draw.rect(window, offblack, (paddleX, 500, 90, 35), 3)
    window.blit(scoreText, (650, 20))
    window.blit(highScoreText, (650, 50))

    pygame.display.update()
