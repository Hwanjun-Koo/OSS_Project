import pygame  
import random

pygame.init()

class Character:

    def __init__(self):
        self.image_path = ''
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5
        self.score = 0

    def set_speed(self):
        pass

    def stop_ball(self):
        pass

    def reset_game(self):
        pass

    def increase_score(self):  # 점수 증가 메서드
        self.score += 1

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

def runGame():
    pygame.init()

    size = [600, 700]
    screen = pygame.display.set_mode(size)

    done = False
    clock = pygame.time.Clock()

    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (size[0], size[1]))
    screen.blit(background_image, (0, 0))

    ball_image = pygame.image.load('ball.png')
    ball_image = pygame.transform.scale(ball_image, (50, 50))
    balls = []

    coin_image = pygame.image.load('coin.png')
    coin_image = pygame.transform.scale(coin_image, (40, 40))
    coins = []

    for i in range(5):
        rect = pygame.Rect(ball_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        balls.append({'rect': rect, 'dy': dy})

    for i in range(4): #ball 개수보다 작은 개수로 3개 생성
        rect = pygame.Rect(coin_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        coins.append({'rect': rect, 'dy': dy})


    selected_character = None
    while selected_character is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_character = "pikachu"
                    pikachu = Pikachu()
                    pikachu.set_speed()
                    speed = pikachu.speed
                    character = pygame.Rect(pikachu.character_image.get_rect())
                elif event.key == pygame.K_2:
                    selected_character = "pyree"
                    pyree = Pyree()
                    speed = pyree.speed
                    character = pygame.Rect(pyree.character_image.get_rect())
                elif event.key == pygame.K_3:
                    selected_character = "kkobugi"
                    kkobugi = Kkobugi()
                    speed = kkobugi.speed
                    character = pygame.Rect(kkobugi.character_image.get_rect())

        pygame.display.flip()
        clock.tick(30)

    character_dx = 0
    character.left = size[0] // 2 - character.width // 2
    character.top = size[1] - character.height


    while not done:
        clock.tick(30)
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_dx = -speed
                elif event.key == pygame.K_RIGHT:
                    character_dx = speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    character_dx = 0
                elif event.key == pygame.K_RIGHT:
                    character_dx = 0


        character.left = character.left + character_dx

        if character.left < 0:
            character.left = 0
        elif character.left > size[0] - character.width:
            character.left = size[0] - character.width

        if selected_character == "pikachu":
            screen.blit(pikachu.character_image, character)
        elif selected_character == "pyree":
            screen.blit(pyree.character_image, character)
        elif selected_character == "kkobugi":
            screen.blit(kkobugi.character_image, character)

        for ball in balls:
            ball['rect'].top += ball['dy']
            if ball['rect'].top > size[1]:
                balls.remove(ball)
                rect = pygame.Rect(ball_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                balls.append({'rect': rect, 'dy': dy})

        for ball in balls:
            if ball['rect'].colliderect(character):
                done = True
            screen.blit(ball_image, ball['rect'])

        for coin in coins:
            coin['rect'].top += coin['dy']
            if coin['rect'].top > size[1] or coin['rect'].colliderect(character):
                coins.remove(coin)
                rect = pygame.Rect(coin_image.get_rect())
                rect.top = -100
                dy = random.randint(3, 9)
                while True:
                    rect.left = random.randint(0, size[0])
                    if not rect.colliderect(character):
                        break
                coins.append({'rect': rect, 'dy': dy})

        for coin in coins:
            if coin['rect'].colliderect(character):
                coins.remove(coin)
                if selected_character == "pikachu":
                    pikachu.increase_score()
                    print('Pikachu score:', pikachu.score)
                elif selected_character == "pyree":
                    pyree.increase_score()
                    print('Pyree score:', pyree.score)
                elif selected_character == "kkobugi":
                    kkobugi.increase_score()
                    print('Kkobugi score:', kkobugi.score)
            screen.blit(coin_image, coin['rect'])

        pygame.display.update()

runGame()
pygame.quit()
