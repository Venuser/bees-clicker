
from pygame.locals import *
import random
import pygame.freetype
pygame.init()

screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.SysFont("Comic Sans MS", 24)
text_surface, rect = GAME_FONT.render("Hello World!", (0, 0, 0))
screen.blit(text_surface, (40, 250))
# Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

pygame.display.set_caption("Bee-Hive")

pygame.mouse.set_visible(1)
pygame.font.init()
pygame.key.set_repeat(1, 30)
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Hive:', False, (0, 0, 0))
screen.blit(textsurface,(20,20))
img_pot = pygame.image.load('C:/Users/Christoph/Codes/Dwarfs/honey.png')
img_hive = pygame.image.load('C:/Users/Christoph/Codes/Dwarfs/hive.png')

#myimage = pygame.image.load(os.path.join("honey.png"))
#imagerect = myimage.get_rect()
# set game variables
count = 0
honey = 0
exp = 0
level = 0
bee = 0
price_bee = 10
queen = 0
price_queen = 200
tick = int(bee) + 1
hive = 0
hive_size = 50
price_hive = 400
price_exp = 100
running = True
lvl_exp = 10

#class bee(object):
#	"""docstring for pet"""
#	def __init__(self, arg):
#		super(pet, self).__init__()
#		self.arg = arg
#	bee = 0		
#class for the drawn bees, work in progress
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

bees1 = bees((0,255,0), 700,100,4,4,'')
clicker = button((0,255,0),100,150, 110, 65, 'click')
buy_bee = button((0,255,0), 700, 240, 40, 40, '+')
buy_hive = button((0,255,0), 200, 10, 40, 40, '+')
buy_queen = button((0,255,0), 700, 290, 40, 40, '+')
buy_exp = button((0,255,0), 700, 500, 40, 40, '+')


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
        		honey = honey - price_bee
        		price_bee += int(bee/2)


        	elif buy_hive.isOver(pos) and honey>=price_hive:
        		hive_size += 50
        		honey -= price_hive
        		price_hive += hive_size/2
        	elif buy_queen.isOver(pos) and honey>=price_queen:
        		queen += 1
        		hive += 5
        		honey -= price_queen
        		price_queen += int(hive_size/2 + price_queen/2)
        	elif buy_exp.isOver(pos) and honey>=price_exp:
        	    exp += 1
        	    honey -= price_exp
         #   if buy_bee.isOver(pos):
          #      bee +=1
           #     price_bee += int(bee/2)
            #    honey = honey - price_bee

    screen.fill((255,255,255))
    honeybee = str(bee)
    score = str(honey)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: running = False
    if pressed[pygame.K_DOWN]: honey += 1
    if pressed[pygame.K_LEFT] and honey>=price_bee:
    	honey = honey - price_bee
    	price_bee += int(bee/3)
    	bee = bee + 1
   		#price_bee = price_bee + if pressed[pygame.K_RIGHT] and honey>=100:
    	#honey = honey - 100
    	#queen = queen + 1
	
	
    #if pressed[pygame.K_RIGHT] and x <=740: x += 3
    if(time%1000 <= 30):
    	honey = honey + bee + 10*(queen)
    	count = count + 1
    	continue

    if(exp == lvl_exp):
    	level += 1
    	exp = 0
    	lvl_exp += lvl_exp/2
    screen.blit(textsurface,(0,0))
    list_bee = [bees((0,255,0), 700+ random.randint(-40,40) ,100+ random.randint(-40,40),4,4,'') for i in range(bee)]
    for i in list_bee:
    	i.draw(screen,(0,0,0)) 
    bees1.draw(screen,(0,0,0))
    clicker.draw(screen,(0,0,0))
    buy_bee.draw(screen,(0,0,0))
    buy_hive.draw(screen,(0,0,0))
    buy_queen.draw(screen,(0,0,0))
    buy_exp.draw(screen,(0,0,0))

    screen.blit(img_pot,(90,100))    
    screen.blit(img_hive,(400,10))

    GAME_FONT.render_to(screen, (100, 15), str(hive), (0, 0, 0))
    GAME_FONT.render_to(screen, (130, 15), '/', (0, 0, 0))

    GAME_FONT.render_to(screen, (150, 15), str(hive_size), (0, 0, 0))

    GAME_FONT.render_to(screen, (30, 350), 'Honey:', (0, 0, 0))
    GAME_FONT.render_to(screen, (130, 350), score, (0, 0, 0))
    GAME_FONT.render_to(screen, (325, 250), 'Worker Bee: #', (0, 0, 0))
    GAME_FONT.render_to(screen, (500, 250), honeybee, (0, 0, 0))
    GAME_FONT.render_to(screen, (575, 250), 'Price:', (0, 0, 0))
    GAME_FONT.render_to(screen, (650, 250), str(price_bee), (0, 0, 0))

    GAME_FONT.render_to(screen, (325, 300), 'Queen Bee: #', (0, 0, 0))
    GAME_FONT.render_to(screen, (500, 300), str(queen), (0, 0, 0))
    GAME_FONT.render_to(screen, (575, 300), 'Price:', (0, 0, 0))
    GAME_FONT.render_to(screen, (650, 300), str(price_queen), (0, 0, 0))

    GAME_FONT.render_to(screen, (375, 500), 'Level:', (0, 0, 0))
    GAME_FONT.render_to(screen, (450, 500), str(level), (0, 0, 0))


    GAME_FONT.render_to(screen, (525, 500), 'EXP:', (0, 0, 0))
    GAME_FONT.render_to(screen, (600, 500), str(exp), (0, 0, 0))
    GAME_FONT.render_to(screen, (630, 500), '/', (0, 0, 0))
    GAME_FONT.render_to(screen, (650, 500), str(lvl_exp), (0, 0, 0))


   # screen.blit(myimage, imagerect)
    pygame.display.flip()

   # clock.tick(60)
