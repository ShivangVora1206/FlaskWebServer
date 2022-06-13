import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.5', 8080))
# s.connect((socket.gethostname(), 8080))
s.send(bytes("hello server", 'utf-8'))
msg = s.recv(1024)
print(msg.decode('utf-8'))
import pygame
from pygame.locals import *

class Choice():
    def __init__(self,label, parent_screen, x, y, width, height, path):    
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.parent_screen = parent_screen
        self.label = label
        self.path = path
        self.block = pygame.image.load(self.path).convert_alpha()
        # self.block = pygame.transform.scale(self.block, (100, 100))
        
    def draw(self, block_type):
        self.block_type = block_type
        if self.block_type == 0:
            pygame.draw.rect(self.parent_screen, (255, 255, 255), (self.x, self.y, self.width+8, self.height+8))
            self.parent_screen.blit(self.block, (self.x, self.y))
        else:
            pygame.draw.rect(self.parent_screen, (110, 114, 120), (self.x, self.y, self.width+8, self.height+8))
            self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.update()

    def is_hover(self, pos):
        self.pos = pos
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Button():
    def __init__(self, x, y, color, width, height, text=""):    
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.text = text
        
    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != "":
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_hover(self, pos):
        self.pos = pos
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Menu():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hand_cricket_with_sockets_client")
        pygame.mixer.init()
        # self.play_background_track()
        self.window = pygame.display.set_mode((1280, 720))
        self.window.fill((255, 255, 255))
        button = Button(515, 310, (0, 255, 255), 250, 100, "PLAY!")

        run = True

        while run:
            self.window.fill((255, 255, 255))
            button.draw(self.window)
            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if  event.type == pygame.MOUSEBUTTONDOWN:
                    if button.is_hover(pos):
                        print("clicked")
                        sound = pygame.mixer.Sound("resources\\menu_select.wav")
                        pygame.mixer.Sound.play(sound)
                        game = Game()
                        game.Run()
                if event.type == pygame.MOUSEMOTION:
                    if button.is_hover(pos):
                        button.color = (82, 255, 209)
                        # sound = pygame.mixer.Sound("resources\\menu_hover.wav")
                        # pygame.mixer.Sound.play(sound)
                    else:
                        button.color = (0, 255, 255)
                        # sound = pygame.mixer.Sound("resources\\menu_hover.wav")
                        # pygame.mixer.Sound.play(sound)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
class Gameover():
    def __init__(self):
        pygame.display.set_caption("Hand_cricket_with_sockets_client")
        # self.play_background_track()
        self.window = pygame.display.set_mode((1280, 720))
        self.window.fill((255, 255, 255))
        button = Button(515, 310, (0, 255, 255), 250, 100, "Back")
        run = True

        while run:
            self.window.fill((255, 255, 255))
            button.draw(self.window)
            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if  event.type == pygame.MOUSEBUTTONDOWN:
                    if button.is_hover(pos):
                        print("clicked")
                        sound = pygame.mixer.Sound("resources\\menu_select.wav")
                        pygame.mixer.Sound.play(sound)
                        menu = Menu()
                if event.type == pygame.MOUSEMOTION:
                    if button.is_hover(pos):
                        button.color = (82, 255, 209)
                        # sound = pygame.mixer.Sound("resources\\menu_hover.wav")
                        # pygame.mixer.Sound.play(sound)
                    else:
                        button.color = (0, 255, 255)
                        # sound = pygame.mixer.Sound("resources\\menu_hover.wav")
                        # pygame.mixer.Sound.play(sound)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1280, 720))
        self.surface.fill((255, 255, 255))
        self.point_x_1 = 173
        self.point_x_2 = 600
        self.point_x_3 = 1027
        self.Score = 0
        self.choice_1 = Choice(1, self.surface, self.point_x_1, 100, 80, 80, "resources\\hand_1.png")
        self.choice_2 = Choice(2, self.surface, self.point_x_2, 100, 80, 80, "resources\\hand_2.png")
        self.choice_3 = Choice(3, self.surface, self.point_x_3, 100, 80, 80, "resources\\hand_3.png")
        self.choice_4 = Choice(4, self.surface, self.point_x_1, 200, 80, 80, "resources\\hand_4.png")
        self.choice_5 = Choice(5, self.surface, self.point_x_2, 200, 80, 80, "resources\\hand_5.png")
        self.choice_6 = Choice(6, self.surface, self.point_x_3, 200, 80, 80, "resources\\hand_6.png")
        self.choice_7 = Choice(7, self.surface, self.point_x_1, 300, 80, 80, "resources\\hand_7.png")
        self.choice_8 = Choice(8, self.surface, self.point_x_2, 300, 80, 80, "resources\\hand_8.png")
        self.choice_9 = Choice(9, self.surface, self.point_x_3, 300, 80, 80, "resources\\hand_9.png")
        self.choice_10 = Choice(10, self.surface, self.point_x_2, 400, 80, 80, "resources\\hand_10.png")
        pygame.display.update()

    def display_score(self, Score):
        self.score = Score
        # self.surface.fill((255, 255, 255))
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f'SCORE:{self.score}', True, (0, 10, 10))
        self.surface.blit(score, (173, 400))
        pygame.display.update()

    def check_game_over(self, label):
        self.curr_lab = label
        s.send(bytes(self.curr_lab, 'utf-8'))
        msg = s.recv(1024)
        print('Server:'+msg.decode('utf-8'))
        if self.curr_lab == msg.decode('utf-8'):
            game_over = Gameover()


    def click_Checker(self, choice, event, label):
        self.choice = choice
        self.label = label
        pos = pygame.mouse.get_pos()
        
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.choice.is_hover(pos):
                print(f"{self.label}")
                self.check_game_over(self.label)
                self.Score += int(self.label)
                self.surface.fill((255, 255, 255))
                self.display_score(self.Score)
                pygame.display.update()
                sound = pygame.mixer.Sound("resources\\menu_select.wav")
                pygame.mixer.Sound.play(sound)
        if event.type == pygame.MOUSEMOTION:
            if self.choice.is_hover(pos):
                self.choice.draw(1)
                pygame.display.update()
                
            elif not self.choice.is_hover(pos):
                self.choice.draw(0)
                pygame.display.update()



    def Run(self):
        self.display_score(self.Score)
        self.choice_1.draw(0)
        self.choice_2.draw(0)
        self.choice_3.draw(0)
        self.choice_4.draw(0)
        self.choice_5.draw(0)
        self.choice_6.draw(0)
        self.choice_7.draw(0)
        self.choice_8.draw(0)
        self.choice_9.draw(0)
        self.choice_10.draw(0)
        pygame.display.update()
        
        self.run = True
        while self.run:
            for event in pygame.event.get():
                self.click_Checker(self.choice_1, event=event, label="1")
                self.click_Checker(self.choice_2, event=event, label="2")
                self.click_Checker(self.choice_3, event=event, label="3")
                self.click_Checker(self.choice_4, event=event, label="4")
                self.click_Checker(self.choice_5, event=event, label="5")
                self.click_Checker(self.choice_6, event=event, label="6")
                self.click_Checker(self.choice_7, event=event, label="7")
                self.click_Checker(self.choice_8, event=event, label="8")
                self.click_Checker(self.choice_9, event=event, label="9")
                self.click_Checker(self.choice_10, event=event, label="10")
                        
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.run = False
            if event.type == QUIT:
                self.run = False
        

menu = Menu()