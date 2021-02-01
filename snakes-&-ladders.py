
import pygame 
import sys  
import random
import time

AQUA = (0,255,255)
BLACK = (0,0,0)
GREEN = (0,128,0)
OLIVE = (128,128,0)
TEAL = (0,128,128)
WHITE = (255,255,255)
pygame.font.init()
smallfont = pygame.font.SysFont('Corbel',45)
# game setup ################ only runs once
pygame.init()  # starts the game engine
screen_width, screen_height = 1500, 900# sets size of screen/window
screen_size = screen_width,screen_height
screen = pygame.display.set_mode(screen_size)# creates window and game screen
background = pygame.image.load("bground.jpg")
screen.blit(background,(0,0))
snakes = pygame.image.load("snake.png")
ladders = pygame.image.load("ladder.png")
time = pygame.time.Clock()
gameState = "running"

counter = 0

def random_color():
    aqua = (118,238,198)
    white = (255,255,255)
    light_red = (255, 100, 100)
    colors = [aqua,white,light_red]
    return random.choice(colors)
print(random_color())
    
def draw_board():
    font = pygame.font.Font(None, 55)
    rows = 100
    cols = 100
    margin = 5
    x = 100
    y = 700
    i = 1
    tile_nums = []

    while i <= 8 and x <= 700 and y == 700:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    y = 600
    i = 8
    x = 100
    while i <= 16 and x <= 700 and y == 600:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    i = 15  
    y = 500
    x = 100
    while i <= 24 and x <= 700 and y == 500:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    i = 22
    y = 400
    x = 100
    while i <= 32 and x<= 700 and y == 400:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    i = 29
    y = 300
    x = 100
    while i <= 40 and x<= 700 and y == 300:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    i = 36
    y = 200
    x = 100
    while i <= 48 and x<= 700 and y == 200:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    i = 43
    y = 100
    x = 100
    while i <= 56 and x<= 700 and y == 100:
        pygame.draw.rect(screen,random_color(),(x,y,rows-margin,cols-margin))
        text = smallfont.render(str(i), True, (0,0,0))
        screen.blit(text,(x,y))
        x += 100
        i += 1
    
    
        
            
print(draw_board())
pygame.display.update()

def click_levels():
    click = pygame.mouse.get_pos()
    if click[0] == 1000 and click[1] == 150:
        n_snakes = 5
        n_ladders = 5
        return [n_snakes, n_ladders]
    elif  click[0] == 1000 and click[1] == 350:
        n_snakes = 10
        n_ladders = 10
        return [n_snakes, n_ladders]
    else:
        n_snakes = 15
        n_ladders = 15
        return [n_snakes, n_ladders]
    time.tick(30) 
        

n = click_levels()
def init_snakes_ladders_board(n):
    keys_lst = []
    for i in range(100,701):
        keys_lst.append(i)
    for i in range(n[0]):
        Snakes = dict.fromkeys(random.choices(keys_lst, weights = None, k = n[0]))
    for key in Snakes:
        Snakes[key] = random.randrange(100,key,100)
        
    for key in keys_lst:
        if key in Snakes:
            keys_lst.remove(key) #ensure ladders dict and snakes dict don't share same coordinates
    for j in range(n[1]):
        Ladders = dict.fromkeys(random.choices(keys_lst, weights = None, k = n[1]))
    for key in Ladders:
        Ladders[key] = random.randrange(key,701,100)
    for key in snake:
        screen.blit(Snakes, (key, Snakes[key]))
    for key in ladder:
        screen.blit(Ladders, (key, Ladders[key]))

        
def click_button():
    click = pygame.mouse.get_pos()
    if click[0] == 1000 and click[1] == 150:
        return init_snakes_ladders_board(n)
    elif click[0] == 1000 and click[1] == 350:
        return init_snakes_ladders_board(n)
    elif click[0] == 1000 and click[1] == 550:
        return init_snakes_ladders_board(n)

        


def roll_die(counter):
    
    if random.randint(1,6) == 1:
        face_1 = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Dice_1.png")
        screen.blit(face_1, (800,700))    
        die = 1
        
        return die
    elif random.randint(1,6) == 2:
        face_2 = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Dice_2.png")
        screen.blit(face_2, (800,700))
        die = 2
        return die
        
    elif random.randint(1,6) == 3:
        face_3 = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Dice_3.png")
        screen.blit(face_3, (800,700))
        die = 3
        return die
    elif random.randint(1,6) == 4:
        face_4 = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Dice_4.png")
        screen.blit(face_4, (800,700))
        die = 4
        return die
    elif random.randint(1,6) == 5:
        face_5 = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Dice_5.png")
        screen.blit(face_5, (800,700))
        die = 5
        return die
    elif random.randint(1,6) == 6:
        face_6 = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Dice_6.png")
        screen.blit(face_6, (800,700))
        die = 6
        return die
    time.tick(50)
    
        
 

while gameState != "exit":        

    Easy = pygame.draw.rect(screen, AQUA, (1000, 150, 300, 100))
    Medium = pygame.draw.rect(screen, AQUA, (1000, 350, 300, 100))
    Hard = pygame.draw.rect(screen, AQUA, (1000, 550, 300, 100))
    
    text = smallfont.render("Easy", True, (255,255,255))
    screen.blit(text,(1000+100,150+50))
    text = smallfont.render("Medium", True, (255,255,255))
    screen.blit(text,(1000+100,350+50))
    text = smallfont.render("Difficult", True, (255,255,255))
    screen.blit(text,(1000+100,550+50))
        

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_levels()
            init_snakes_ladders_board(n)
            click_button()
    
        
    counter = roll_die(counter)
    pos = []
    player = 1

    def turn_player_1(counter,pos,player):
        play_piece = pygame.image.load("/Users/mashaalyusufi/Desktop/DSA_game/Snakes_ladders_pieces.png")
        piece_x = 150
        piece_y = 750
        screen.blit(play_piece,(piece_x,piece_y))    #play piece moves across board
        if counter == 1 and player % 8 != 0:
            player += counter #steps player has moved
            piece_x += 100
#             enqueue(pos,player)
            
            screen.blit(play_piece,(piece_x+100,piece_y))
#             dequeue(pos)
        elif counter == 2 and player % 8 != 0:
            player += counter
            piece_x += 200
#             enqueue(pos,player)
            
#             screen.blit(play_piece(x+200,y))
#             dequeue(pos)
        elif counter == 3 and player % 8 != 0:
            player += counter
            piece_x += 300
#             enqueue(pos,player)
#             screen.blit(play_piece(x+300,y))
#             dequeue(pos)
        elif counter == 4 and player % 8 != 0:
            player += counter
            piece_x += 400
#             enqueue(pos,player)
#             screen.blit(play_piece(x+400,y))
#             dequeue(pos)
        elif counter == 5 and player % 8 != 0:
            player += counter
            piece_x += 500
#             enqueue(pos,player)
#             screen.blit(play_piece(x+500,y))
#             dequeue(pos)
        elif counter == 6 and player % 8 != 0:
            player += counter
            piece_x += 600
#             enqueue(pos,player)
#             screen.blit(play_piece(x+600,y))
#             dequeu(pos)
        elif player % 8 == 0:
            player += counter
            piece_y = piece_y - 100
#             enqueue(pos,player)
           
#             screen.blit(x,y-100)
#             dequeue(pos)
           
            
    print(turn_player_1(counter,pos,player))
    pygame.display.update()

    
    


    
    #Stack and Queue Operations
    def push(lst,data): return lst.append(data)
    def top(lst): return lst[-1]
    def pop(lst): return lst.pop()
    def is_empty(lst): return len(lst)==0
    def enQueue(lst,data): return lst.append(data)
    def front(lst): return lst[0]
    def deQueue(lst): return lst.pop(0)

    
    lst = []
    data = 0
    def enqueue(lst,data):
        return lst.append(pos)
    
    def dequeue(lst):
        return lst.pop(0)
    
     


    # code ends here
    pygame.display.update()
    pygame.display.flip()  

    


print("The game has closed")  
pygame.quit()  
sys.exit()  
