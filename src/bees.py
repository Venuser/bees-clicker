
from pygame.locals import *
import random
import pygame.freetype
import thorpy


pygame.init()

screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.SysFont("Comic Sans MS", 24)

# Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

pygame.display.set_caption("Bee-Hive")

pygame.mouse.set_visible(1)
pygame.font.init()
pygame.key.set_repeat(1, 30)
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Hive:', False, (0, 0, 0))
screen.blit(textsurface,(20,20))

#-------------------SET PATH TO WHERE YOU HAVE SAVED THE FOLDER BEES---------------
#img_pot = pygame.image.load('C:/Users/Christoph/Codes/bees/honey.png')
img_hive = pygame.image.load('C:/Users/Christoph/Codes/bees/hive.png')
img_background = pygame.image.load('C:/Users/Christoph/Codes/bees/background.png')
#myimage = pygame.image.load(os.path.join("honey.png"))
#imagerect = myimage.get_rect()
# set game variables
count = 0
honey = 0
exp = 0
level = 0
bee = 1
queen = 0
honey_bee = 0

tick = int(bee) + 1
hive = 0
hive_size = 50

price_honey_bee = 3000
price_queen = 200
price_bee = 10
price_hive = 400
price_exp = 100

running = True

lvl_exp = 10
evolution = 0

list_bee = []
list_queen = []
list_honeybee = []


class bees():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x + random.randint(-2,2)
        self.y = y + random.randint(-2,2)
        self.width = width
        self.height = height
        self.text = text
    def draw(self,win,outline=None):
    #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        self.x += random.randint(-2,2)  
        self.y += random.randint(-2,2)    
        pygame.draw.rect(win, self.color, (self.x+random.randint(-2,2),self.y+random.randint(-2,2),self.width,self.height),0)
    
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
# class for the buttons
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class popup():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.text = text

class upgrade_screen():
    def upgrades():
        screen = pygame.display.set_mode((800, 600))
        run = True
        while run:
            screen.fill(white)
            GAME_FONT.render_to(screen, (111, 111), 'tewsta:', (0, 0, 0))

            pygame.display.flip()




    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def my_alert_1():
    thorpy.launch_nonblocking_alert(title="This is a non-blocking alert!",
                                text="This is the text..",
                                ok_text="Ok, I've read",
                                font_size=12,
                                font_color=(255,0,0))
    print("Proof that it is non-blocking : this sentence is printing at exit!")



#button1 = thorpy.make_button("Non-blocking alert", func=my_alert_1)
#declaration of some ThorPy elements ...
#slider = thorpy.SliderX(100, (12, 35), "My Slider")
#button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
#box = thorpy.Box(elements=[slider,button])
#we regroup all elements on a menu, even if we do not launch the menu
#menu = thorpy.Menu(box)
#important : set the screen as surface for all elements
#for element in menu.get_population():
 #   element.surface = screen
#use the elements normally...
#box.set_topleft((100,100))
#box.blit()
#box.update()


bees1 = bees((255,255,0), 500,300,4,4,'')
clicker = button((255,255,0), 175, 450, 110, 65, 'click')
buy_bee = button((255,255,0), 750, 40, 40, 40, '+')
buy_hive = button((255,255,0), 200, 10, 40, 40, '+')
buy_queen = button((255,255,0), 750, 90, 40, 40, '+')
buy_exp = button((255,255,0), 725, 540, 40, 40, '+')
buy_honey_bee = button((255,255,0), 750, 140, 40, 40, '+')
upgrade_button = button((255,255,0), 25, 550, 250, 40, 'Evolutions')
#main loop
while running:
    time = pygame.time.get_ticks()
    # Framerate auf 30 Frames pro Sekunde beschränken.

    # Pygame wartet, falls das Programm schneller läuft.
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

            # all click events for buttons etc.
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if clicker.isOver(pos):
                honey += 1



            elif buy_bee.isOver(pos) and honey>=price_bee and hive<hive_size:
                bee +=1 
                hive += 1
                list_bee.append(bees((255,255,0), 500 + random.randint(-40,40), 300 + random.randint(-40,40),2,2,''))
                honey = honey - price_bee
                price_bee += int(bee/2)

            elif buy_hive.isOver(pos) and honey>=price_hive:
                hive_size += 50
                honey -= price_hive
                price_hive += int(price_hive*hive_size/2)
            elif buy_queen.isOver(pos) and honey>=price_queen and hive+5<hive_size:
                queen += 1
                hive += 5
                honey -= price_queen
                price_queen += int(hive_size/2 + price_queen/2)
                list_queen.append(bees((255,255,0), 500 + random.randint(-40,40), 300 + random.randint(-40,40),8,4,''))

            elif buy_exp.isOver(pos) and honey>=price_exp:
                exp += 1
                honey -= price_exp
            elif buy_honey_bee.isOver(pos) and honey>=price_honey_bee and hive+10<=hive_size:
                honey_bee += 1
                hive += 10
                honey -= price_honey_bee
                price_honey_bee += int(price_honey_bee/2)
                list_honeybee.append(bees((255,255,0), 500 + random.randint(-40,40), 300 + random.randint(-40,40),8,8,''))

            elif upgrade_button.isOver(pos):
                screen1 = upgrade_screen()
                screen1.upgrades


       

    screen.fill((255,255,255))
    screen.blit(img_background, (0,0))

    honeybee = str(bee)
    score = str(honey)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: running = False
    if pressed[pygame.K_DOWN]: honey += 100
    if pressed[pygame.K_LEFT] and honey>=price_bee:
        honey = honey - price_bee
        price_bee += int(bee/3)
        bee = bee + 1
        #price_bee = price_bee + if pressed[pygame.K_RIGHT] and honey>=100:
        #honey = honey - 100
        #queen = queen + 1
    
    
    #if pressed[pygame.K_RIGHT] and x <=740: x += 3
    if(time%1000 <= 30):
        honey = honey + bee + 10*(queen) + 100*honey_bee
        count = count + 1
        continue

    if(exp == lvl_exp):
        evolution += 1
        level += 1
        exp = 0
        lvl_exp += int(lvl_exp/2)
    screen.blit(textsurface,(0,0))
    #list_bee = [bees((255,255,0), 500 + random.randint(-40,40), 300 + random.randint(-40,40),4,4,'') for i in range(bee)]


    for i in list_bee:
        i.draw(screen,(0,0,0)) 
    for i in list_queen:
        i.draw(screen,(0,0,0)) 
    for i in list_honeybee:
        i.draw(screen,(0,0,0)) 
    #draw buttons
    bees1.draw(screen,(0,0,0))
    #clicker.draw(screen,(0,0,0))
    buy_bee.draw(screen,(0,0,0))
    buy_hive.draw(screen,(0,0,0))
    buy_queen.draw(screen,(0,0,0))
    buy_honey_bee.draw(screen,(0,0,0))
    buy_exp.draw(screen,(0,0,0))
    upgrade_button.draw(screen,(0,0,0))

    #blit images
    #pip install thorpyl
   # screen.blit(img_pot,(90,100))    
  
  #  screen.blit(img_hive,(400,10))

    #draw scores, labels etc.

    GAME_FONT.render_to(screen, (100, 15), str(hive), (0, 0, 0))
    GAME_FONT.render_to(screen, (135, 15), '/', (0, 0, 0))
    GAME_FONT.render_to(screen, (150, 15), str(hive_size), (0, 0, 0))
    GAME_FONT.render_to(screen, (25, 40), 'Price:', (0, 0, 0))
    GAME_FONT.render_to(screen, (100, 40), str(price_hive), (0, 0, 0))



    GAME_FONT.render_to(screen, (30, 400), 'Honey:', (0, 0, 0))
    GAME_FONT.render_to(screen, (130, 400), score, (0, 0, 0))
    GAME_FONT.render_to(screen, (30, 450), 'HPS:', (0, 0, 0))
    GAME_FONT.render_to(screen, (130, 450), str(bee+10*queen+ 100*honey_bee), (0, 0, 0))

    GAME_FONT.render_to(screen, (325, 50), 'Worker Bee: #', (0, 0, 0))
    GAME_FONT.render_to(screen, (500, 50), honeybee, (0, 0, 0))
    GAME_FONT.render_to(screen, (575, 50), 'Price:', (0, 0, 0))
    GAME_FONT.render_to(screen, (650, 50), str(price_bee), (0, 0, 0))

    GAME_FONT.render_to(screen, (325, 100), 'Queen Bee: #', (0, 0, 0))
    GAME_FONT.render_to(screen, (500, 100), str(queen), (0, 0, 0))
    GAME_FONT.render_to(screen, (575, 100), 'Price:', (0, 0, 0))
    GAME_FONT.render_to(screen, (650, 100), str(price_queen), (0, 0, 0))


    GAME_FONT.render_to(screen, (325, 150), 'Honey Bee: #', (0, 0, 0))
    GAME_FONT.render_to(screen, (500, 150), str(honey_bee), (0, 0, 0))
    GAME_FONT.render_to(screen, (575, 150), 'Price:', (0, 0, 0))
    GAME_FONT.render_to(screen, (650, 150), str(price_honey_bee), (0, 0, 0))

    GAME_FONT.render_to(screen, (400, 550), 'Level:', (0, 0, 0))
    GAME_FONT.render_to(screen, (475, 550), str(level), (0, 0, 0))


    GAME_FONT.render_to(screen, (550, 550), 'EXP:', (0, 0, 0))
    GAME_FONT.render_to(screen, (625, 550), str(exp), (0, 0, 0))
    GAME_FONT.render_to(screen, (655, 550), '/', (0, 0, 0))
    GAME_FONT.render_to(screen, (685, 550), str(lvl_exp), (0, 0, 0))


   # screen.blit(myimage, imagerect)
   # menu.react(event) #the menu automatically integrate your elements        
    pygame.display.flip()

   # clock.tick(60)
