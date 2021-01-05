import pygame
import sys
import math
import random

WIDTH = 1200
HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (204, 0, 153)
YELLOW = (255, 255, 0)
PINK = (255, 102, 128)

pygame.init()
pygame.display.set_caption("Breakout to Earth")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.png") #r"F:\.vscode\python_course\project\background.png"
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Paddle():
    def __init__(self):
        self.x = WIDTH/2.0
        self.y = 700
        self.dx = 0
        self.width = 180
        self.height = 10
        self.score = 0

    def left(self):
        self.dx = -12
    
    def right(self):
        self.dx = 12
    
    def move(self):
        self.x = self.x + self.dx
        
        if self.x < 0 + self.width/2.0:
            self.x = 0 + self.width/2.0
            self.dx = 0
        
        elif self.x > WIDTH - self.width/2.0:
            self.x = WIDTH - self.width/2.0
            self.dx = 0
        
    def render(self):
        pygame.draw.rect(screen, PURPLE, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 

class Ball():
    def __init__(self):
        self.x = WIDTH/2.0
        self.y = 600
        self.dx = 6
        self.dy = -6
        self.width = 15
        self.height = 15
    
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        if self.x < 0 + self.width/2.0:
            self.x = 0 + self.width/2.0
            self.dx *= -1
        
        elif self.x > WIDTH - self.width/2.0:
            self.x = WIDTH - self.width/2.0
            self.dx *= -1
            
        if self.y < 0 + self.height/2.0:
            self.y = 0 + self.height/2.0
            self.dy *= -1
        
        elif self.y > HEIGHT - self.height/2.0:
            self.y = HEIGHT - self.height/2.0
            self.x = WIDTH / 2.0
            self.y = HEIGHT / 2.0
            
        
    def render(self):
        pygame.draw.rect(screen, RED, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 

    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 22
        self.color = random.choice([YELLOW, GREEN, BLUE, PINK])
        
    def render(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 


font = pygame.font.SysFont("impact", 48)


hit_sound = pygame.mixer.Sound("hit.wav") #r"F:\.vscode\python_course\project\hit.wav"


paddle = Paddle()
ball = Ball()

bricks = []
for y in range(100, 375, 25):
    color = random.choice([YELLOW, GREEN, BLUE, PINK])
    for x in range(25, 1200, 50):
        bricks.append(Brick(x, y))
        bricks[-1].color = color


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.left()
            elif event.key == pygame.K_RIGHT:
                paddle.right()

    paddle.move()
    ball.move()
    
    if ball.is_aabb_collision(paddle):
        ball.dy *= -1
        hit_sound.play()
    
    dead_bricks = []
    for brick in bricks:
        if ball.is_aabb_collision(brick):
            ball.dy *= -1
            dead_bricks.append(brick)
            paddle.score += 5
            hit_sound.play()
            
    for brick in dead_bricks:
        bricks.remove(brick)
        
    if len(bricks) <= 0:
        print("YOU WIN!")
        
    BackGround = Background("background.png", [0,0]) #r"F:\.vscode\python_course\project\background.png"
    screen.fill(BLACK)
    screen.blit(BackGround.image, BackGround.rect)
    
    paddle.render()
    ball.render()
    
    for brick in bricks:
        brick.render()
     
    score_surface = font.render(f"Score: {paddle.score}", True, WHITE)
    screen.blit(score_surface, (WIDTH/2.0 - 75, 10))

    pygame.display.flip()
    
    clock.tick(60)
