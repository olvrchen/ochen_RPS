# file created by: Oliver Chen

# import libraries


from time import sleep
from random import randint
import pygame as pg
import os

userchoice = ""
#  setup assent folders - images
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settins
WIDTH = 1500
HEIGHT = 950
FPS = 30


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("RosPaperScissors")
clock = pg.time.Clock()
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
yes_image = pg.image.load(os.path.join(game_folder, 'yes.jpg')).convert()
no_image = pg.image.load(os.path.join(game_folder, 'no.jpg')).convert()

# creates transparency
rock_image.set_colorkey(WHITE)
paper_image.set_colorkey(WHITE)
scissors_image.set_colorkey(WHITE)
yes_image.set_colorkey(WHITE)
no_image.set_colorkey(WHITE)

# the choices that the player and computer has to chose
choices = ["rock", "paper", "scissors"]

rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
yes_rect = scissors_image.get_rect()
no_rect = scissors_image.get_rect()
# these lines of code 
rock_rect.x = 20
paper_rect.x = WIDTH/3 + 100
paper_rect.y = 100
yes_rect.x = 1200
yes_rect.y = 650
no_rect.y = 650
scissors_rect.x = WIDTH/1.5 + 200

'''this funtions makes the computer choice form the list: choices'''
def cpu_choice():
    # this returns a random integer from 0, 1, or 2 and goes into the list: choices
    return choices[randint(0,2)]

'''this function asks the player if they want to play again'''
def wannaplay():
    screen.fill(WHITE)
    play = font.render("Do you want to play again", True, BLACK)
    screen.blit(play, (380, HEIGHT/2 + 175))
    mouse_coords1 = pg.mouse.get_pos()
    '''displays the yes and no image for the user to click on'''
    screen.blit(yes_image, yes_rect)
    screen.blit(no_image, no_rect)
    '''if user clicks on checkmark, the code will run again'''
    # going = True
    # while going == True:
    if yes_rect.collidepoint(mouse_coords1):
        imgs()
        # else:
        #     going = False
    

def rps():
    # prints the choice that the cpu chose
    # print("The computer chose", cpu)
    # the next few if and elif loops are the logic of the 
    if userchoice == cpu:
        print("YOU TIE!")
        tie = font0.render("YOU TIE", True, BLACK)
        screen.blit(tie, (400, HEIGHT/2 + 175))
    elif userchoice == "rock" and cpu == "scissors":
        print("YOU WIN, WINNER!")
        win = font0.render("YOU WIN", True, BLACK)
        screen.blit(win, (400, HEIGHT/2 + 175))
    elif userchoice == "paper" and cpu == "rock":
        print("YOU WIN, WINNER!")
        win = font0.render("YOU WIN", True, BLACK)
        screen.blit(win, (400, HEIGHT/2 + 175))
    elif userchoice == "scissors" and cpu == "paper":
        print("YOU WIN, WINNER!")
        win = font0.render("YOU WIN", True, BLACK)
        screen.blit(win, (400, HEIGHT/2 + 175))
    elif userchoice == "rock" and cpu == "paper":
        print("YOU LOSE, LOSER!")
        lose = font0.render("YOU LOSE", True, BLACK)
        screen.blit(lose, (400, HEIGHT/2 + 175))
    elif userchoice == "scissors" and cpu == "rock":
        print("YOU LOSE, LOSER!")
        lose = font0.render("YOU LOSE", True, BLACK)
        screen.blit(lose, (400, HEIGHT/2 + 175))
    elif userchoice == "paper" and cpu == "scissors":
        print("YOU LOSE, LOSER!")
        lose = font0.render("YOU LOSE", True, BLACK)
        screen.blit(lose, (400, HEIGHT/2 + 175))
    else:
        print("Somethin ain't right")

font = pg.font.SysFont("exima_geometric.ttc", 92)
font0 = pg.font.SysFont("exima_geometric.ttc", 200)
img2 = font.render("What do you want?", True, BLUE) 

'''this shows what the options the player has to pick'''   
img3 = font.render("rock,", True, BLUE)  
img4 = font.render("paper,", True, BLUE)  
img5 = font.render("or,", True, BLUE)  
img6 = font.render("scissors", True, BLUE)  

'''these lines show what the player has chosen to play with'''
img7 = font.render("You chose rock", True, BLACK)   
img8 = font.render("You chose paper", True, BLACK)   
img9 = font.render("You chose scissors", True, BLACK) 
img10 = font.render("You clicked on empty space...", True, BLACK) 

'''these lines show what the computer has chosen'''
cpuchoice0 = font.render("The computer chose rock", True, BLACK)
cpuchoice1 = font.render("The computer chose paper", True, BLACK)
cpuchoice2 = font.render("The computer chose scissors", True, BLACK)

'''the win lose and tie displays'''
win = font0.render("YOU WIN", True, BLACK)
lose = font0.render("YOU LOSE", True, BLACK)
tie = font0.render("YOU TIE", True, BLACK)

'''displays everything onto the screen'''
def imgs():
    screen.fill(WHITE)
    screen.blit(scissors_image, scissors_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(rock_image, rock_rect)
    screen.blit(img2, (WIDTH/4, 550))
    screen.blit(img3, (300, 650))
    screen.blit(img4, (470, 650))
    screen.blit(img5, (680, 650))
    screen.blit(img6, (770, 650))

running = True
while running:
    clock.tick(FPS)
    imgs()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            cpu = cpu_choice()
            '''the logic after the rock is clicked'''
            if rock_rect.collidepoint(mouse_coords):
                # print("you clicked on rock")
                userchoice = "rock"
                screen.fill(WHITE)
                screen.blit(img7, (450, HEIGHT/4))
                if cpu == "rock":
                    screen.blit(cpuchoice0, (350, HEIGHT/2)) 
                elif cpu == "paper":
                    screen.blit(cpuchoice1, (350, HEIGHT/2)) 
                elif cpu == "scissors":
                    screen.blit(cpuchoice2, (350, HEIGHT/2))
            elif paper_rect.collidepoint(mouse_coords):
                # print("you clicked on paper")
                userchoice = "paper"
                screen.fill(WHITE)
                screen.blit(img8, (450, HEIGHT/4))                
                if cpu == "rock":
                    screen.blit(cpuchoice0, (350, HEIGHT/2)) 
                elif cpu == "paper":
                    screen.blit(cpuchoice1, (350, HEIGHT/2)) 
                elif cpu == "scissors":
                    screen.blit(cpuchoice2, (350, HEIGHT/2))                
            elif scissors_rect.collidepoint(mouse_coords):
                # print("you clicked on scissors")
                userchoice = "scissors"
                screen.fill(WHITE)
                screen.blit(img9, (450, HEIGHT/4))
                if cpu == "rock":
                    screen.blit(cpuchoice0, (350, HEIGHT/2)) 
                elif cpu == "paper":
                    screen.blit(cpuchoice1, (350, HEIGHT/2)) 
                elif cpu == "scissors":
                    screen.blit(cpuchoice2, (350, HEIGHT/2))
            else:
                # print("you clicked on empty space...")
                userchoice = "empty"
                screen.fill(WHITE)  
                screen.blit(img10, (WIDTH/6, HEIGHT/2)) 

            rps()
            pg.display.flip()  
            sleep(2)
            wannaplay()
        pg.display.flip()
            

pg.quit()