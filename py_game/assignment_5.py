import pygame
import os
import random

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("assignment_5")

FPS = 60
VEL = 5
GEAR_VEL = 2

ROBOT_WIDTH, ROBOT_HEIGHT = 110, 80  
GEAR_WIDTH, GEAR_HEIGHT = 40, 30  

pygame.mixer.init()

ROBOT_IMAGE = pygame.image.load(os.path.join('Assets', 'pixel-robot', 'robot-preview.png'))
ROBOT = pygame.transform.scale(ROBOT_IMAGE, (ROBOT_WIDTH, ROBOT_HEIGHT))

GEAR_IMAGE = pygame.image.load(os.path.join('Assets', 'gear.png'))
GEAR = pygame.transform.scale(GEAR_IMAGE, (GEAR_WIDTH, GEAR_HEIGHT))

BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'background.png'))
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

pygame.mixer.music.load(os.path.join('Assets', 'theme.mp3'))
pygame.mixer.music.play(-1, 0.0)

class FOOD:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, GEAR_WIDTH, GEAR_HEIGHT)  # Use GEAR_WIDTH and GEAR_HEIGHT for gear size
        self.vel = GEAR_VEL
    
    def update(self):
        self.rect.x -= self.vel
        
    def draw(self, window):
        window.blit(GEAR, (self.rect.x, self.rect.y))
    
    def is_off_screen(self):
        return self.rect.x < -GEAR_WIDTH  # Check if the gear goes off the screen
    
    def check_collision(self, robot_rect):
        return self.rect.colliderect(robot_rect)

def draw_window(robot, food_list):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(ROBOT, (robot.x, robot.y)) 
    
    for food in food_list:
        food.draw(WIN)
        
    pygame.display.update()

def yellow_handle_movement(keys_pressed, robot):
    if keys_pressed[pygame.K_LEFT] and robot.x - VEL > 0:
        robot.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and robot.x + VEL + robot.width < WIDTH:
        robot.x += VEL
    if keys_pressed[pygame.K_UP] and robot.y - VEL > 0:
        robot.y -= VEL
    if keys_pressed[pygame.K_DOWN] and robot.y + VEL + robot.height < HEIGHT:
        robot.y += VEL

def main():
    robot = pygame.Rect(100, 300, ROBOT_WIDTH, ROBOT_HEIGHT)
    food_list = []

    food_spawn_timer = 0
    food_spawn_delay = 120

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Spawn food at intervals
        food_spawn_timer += 1
        if food_spawn_timer >= food_spawn_delay:
            new_food = FOOD(WIDTH, random.randint(50, HEIGHT - GEAR_HEIGHT - 50))
            food_list.append(new_food)
            food_spawn_timer = 0

        # Update food and check for collisions
        for food in food_list[:]:
            food.update()
            if food.is_off_screen():
                food_list.remove(food)

            if food.check_collision(robot):
                food_list.remove(food)  # Remove the food upon collision
        
        # Handle robot movement
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, robot)

        # Draw everything
        draw_window(robot, food_list)
        
    pygame.quit()

if __name__ == "__main__": 
    main()
