import pygame
import random
from platforms import Platform 

#pygame boilerplayer setup
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Base Dash Clone")
clock = pygame.time.Clock() #controls frame rate

#important game variables
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK = (0, 0, 51)




#Player variables
pw, ph = 10, 20 #player width and height
px, py = 50, 50 #inital player position
vx, vy = 5, 0 #velocity x and y
g = 0.5 #gravity
jmp = -10 #normal jumper power
double_jmp = -15 #stronger double jump power
jumping = False #Keeps track of wheather you're in the air
double_jump = False #Flag to track if the player has used double jump
jump_pressed = False #Track whether the jump key has been pressed

#load player animation frames
walk1 = pygame.image.load('Walk 1.png')
walk2 = pygame.image.load('Walk 2.png')

#Animation variables
current_frame = 0 #Start with the first frame
animation_speed = 0.1 #contols how fast the animation changes
frame_timer = 0 #Timer to track when to switch frames

platforms = [] #list to hold all platforms


while True: #Game loop-------------------------------------------------------------
    clock.tick(60)
    
    #Event handling section/input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    
    #physics section/update
    
#platform stuff----------------------------------------------------------------------
    #platform creation and destruction
    if random.randint(1, 100) <= 7: #Random chance to create a new platform
        platforms.append(Platform())
        print("apeending platform!")
        
    #remove platforms that have moved off screen
    for platform in platforms:
        if platform.x + platform.width < 50: #check if the platform is off the screen
            platforms.remove(platform) #fun fact: if this was C++, we'd need to use a destructor
            
    for platform in platforms:
        platform.update()
    
    
#player stuff-------------------------------------------------------------------------
    #player movement
    if keys[pygame.K_LEFT]:
        px -= vx
        
    elif keys[pygame.K_RIGHT]:
        px += vx
        
    #Jumping logic
    if keys[pygame.K_UP]:
        if not jump_pressed:
            if not jumping:
                vy = jmp
                jumping = True
            elif not double_jump:
                vy = double_jmp #use stronger double jump power
                double_jump = True
            jump_pressed = True
        else:
            jump_pressed = False #Reset the jump pressed flag when the key is released 
        
    #Apply gravity
    vy += g
    py += vy
    
    #Check if the player is on the ground
    if py >= 600 - ph:
        py = 600 - ph
        jumping = False
        vy = 0

    
    #Animation logic
    frame_timer += animation_speed
    if frame_timer >= 1:
        frame_timer = 0
        current_frame = (current_frame + 1) % 2 #switch between frame 0 and 1
        
    #choose the correct frame
    if current_frame == 0:
        current_image = walk1
    else:
        current_image = walk2
        
    #-render section------------------------------------------------------------------
    screen.fill(DARK)
    
    pygame.draw.rect(screen, BLUE, (px, py, pw, ph)) #Draw the player
    
    for platform in platforms:
        platform.draw(screen)
    
    pygame.display.flip() #Update the display

#end of game loop------------------------------------------------------------------
    
    
        
