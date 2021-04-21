import pygame  #import the libary(is necessary for download)

MAX_X = 800
MAX_Y = 600  #the size of the main screen
IMG_SIZE = 100
game_over = False
x = 500  #position of the image
y = 100
bg_color = (0, 0, 100)  #the variable for background color

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("PyGame Game")  #set up the name of the screen

myimage = pygame.image.load("stacklogo.png").convert()  #dowload the image and convert it
myimage = pygame.transform.scale(myimage, (IMG_SIZE, IMG_SIZE))  #transform the image to another size

move_up = False  #the variables for moving the picture
move_down = False
move_right = False
move_left = False

#---the main game loop----
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type  == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  #change the position of the image with the mouse

    if move_left == True:
        x -= 1
        if x < 0:  #check the possibility if we can go outside of the screen, left side
            x = 0
    if move_right == True:
        x += 1
        if x > MAX_X-IMG_SIZE:
            x = MAX_X-IMG_SIZE
    if move_up == True:
        y -= 1
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        if y > MAX_Y-IMG_SIZE:
            y = MAX_Y-IMG_SIZE

    screen.fill(bg_color)  #change of the background color
    screen.blit(myimage, (x, y))  #show the image on the necessary position
    pygame.display.flip()