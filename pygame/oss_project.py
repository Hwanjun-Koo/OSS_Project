import pygame  
import random
import os

pygame.init()  

class Character:

    def __init__(self):
        self.image_path = ''
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5
    
    def set_speed(self):
        pass

    def stop_ball(self):
        pass

    def reset_game(self):
        pass

class Pikachu(Character):
    def __init__(self):
        self.image_path = 'pikachu.png'
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5

    def set_speed(self):
        self.speed = 10

class Pyree(Character):
    def __init__(self):
        self.image_path = 'pyree.png'
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5

    def stop_ball(self):
        pass

class Kkobugi(Character):
    def __init__(self):
        self.image_path = 'kkobugi.png'
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5
    
    def reset_game(self):
       pass

BLACK = (0, 0, 0)
size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    ball_image = pygame.image.load('ball.png')
    ball_image = pygame.transform.scale(ball_image, (50, 50))
    balls = []

    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, size[0], size[1])

    screen.blit(background_image, (0, 0))

    for i in range(5):
        rect = pygame.Rect(ball_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        balls.append({'rect': rect, 'dy': dy})

    character_image = pygame.image.load('person.png')
    character_image = pygame.transform.scale(character_image, (100, 100))
    character = pygame.Rect(character_image.get_rect())
    character.left = size[0] // 2 - character.width // 2
    character.top = size[1] - character.height
    character_dx = 0
    character_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_dx = -5
                elif event.key == pygame.K_RIGHT:
                    character_dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    character_dx = 0
                elif event.key == pygame.K_RIGHT:
                    character_dx = 0

        for ball in balls:
            ball['rect'].top += ball['dy']
            if ball['rect'].top > size[1]:
                balls.remove(ball)
                rect = pygame.Rect(ball_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                balls.append({'rect': rect, 'dy': dy})

        character.left = character.left + character_dx

        if character.left < 0:
            character.left = 0
        elif character.left > size[0] - character.width:
            character.left = size[0] - character.width

        screen.blit(character_image, character)

        for ball in balls:
            if ball['rect'].colliderect(character):

                done = True
            screen.blit(ball_image, ball['rect'])

        pygame.display.update()


runGame()
pygame.quit()
