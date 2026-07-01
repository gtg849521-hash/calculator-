import pygame, sys, random
from pygame.math import Vector2
class snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 1)
        self.head_up = pygame.image.load("head_up.png").convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.image.load("head_down.png").convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.image.load("head_right.png").convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.image.load("head_left.png").convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))

        self.tail_up = pygame.image.load("tail_up.png").convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.image.load("tail_down.png").convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.image.load("tail_right.png").convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.image.load("tail_left.png").convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))

        self.body_vertical = pygame.image.load("body_up.png").convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (cell_size, cell_size))
        self.body_horizontal = pygame.image.load("body_strth.png").convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (cell_size, cell_size))

        self.body_tr = pygame.image.load("tr.png").convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr, (cell_size, cell_size))
        self.body_tl = pygame.image.load("tl.png").convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl, (cell_size, cell_size))
        self.body_br = pygame.image.load("br.png").convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br, (cell_size, cell_size))
        self.body_bl = pygame.image.load("bl.png").convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl, (cell_size, cell_size))
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    
            
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy
           
class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)
class MAIN:
    def __init__(self):
        self.snake = snake()
        self.fruit = Fruit()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit()
            self.snake.body.append(self.snake.body[-1])
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
pygame.init()
cell_num = 20
cell_size = 20
screen = pygame.display.set_mode((cell_num * cell_size, cell_num * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (cell_size, cell_size))
main_game = MAIN()
test_surface = pygame.Surface((100, 50))
test_surface.fill(pygame.Color('red'))#fills the surface with color
x_pos = 100 
y_pos = 50
test_rect = test_surface.get_rect(center = (200, 250)) #pygame.Rect(200,100, 100, 100)#creates a rectangle with the surface
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)#every 150 milliseconds the screen will update
while True:
    #all elements of the game will be here 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()#allows to close the window
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
    screen.fill(pygame.Color('white'))#adds color RGB tuple is how much of red green and blue 
    main_game.fruit.draw_fruit()
    main_game.snake.draw_snake()
    #pygame.draw.rect(screen,pygame.Color("green"),test_rect)#draws the rectangle on the screen   
    #test_rect.x += 1 #moves the rectangle to the right
    #screen.blit(test_surface,test_rect)
    #screen.blit(test_surface, (x_pos, y_pos))#blit is used to draw the surface on the screen
    pygame.display.update()#keeps the screen on 
    clock.tick(60)#framerate
