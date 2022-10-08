import pygame

from dino_runner.utils.constants import DUCKING_SHIELD, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD, SHIELD_TYPE, JUMPING_HAMMER, HAMMER_TYPE, HAMMER, RUNNING_HAMMER, DUCKING_HAMMER
from dino_runner.utils.constants import JUMPING
from dino_runner.utils.constants import DUCKING, DEFAULT_TYPE
from dino_runner.utils.constants import RUNNING

from pygame.sprite import Sprite

DUCK_IMG = {DEFAULT_TYPE : DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

FONT_STYLE = 'freesansbold.ttf'

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5
    POS_DUCK = 340

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.image_hammer = HAMMER
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jum = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        self.hammer_vel = 10
        self.hammer_rect = HAMMER.get_rect()
        self.hammer_rect.y = 310
        self.hammer_rect.x = 90
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False
        self.show_text = False
        self.shield_time_up = 0


    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jum:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jum and not self.dino_duck:
            self.dino_jum = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jum:
            self.dino_jum = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jum and not user_input[pygame.K_DOWN]:
            self.dino_jum = False
            self.dino_run = True
            self.dino_duck = False
        
        if self.hammer:
            if user_input[pygame.K_RIGHT]:
                self.athrow_hammer()

        
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jum:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jum = False
            self.jump_vel = self.JUMP_VEL    

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.POS_DUCK
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x , self.dino_rect.y))
        if self.hammer:
            screen.blit(self.image_hammer, (self.hammer_rect.x , self.hammer_rect.y))

    
    def check_invicibility(self, screen):
        if self.shield == True:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 100, 2)
            if time_to_show >= 0 and self.show_text:
                font = pygame.font.Font(FONT_STYLE,30)
                text = font.render(f"Time to Power Up: {time_to_show}", True, (0,0,0))
                text_rect = text.get_rect()
                text_rect.center = (400, 50)
                screen.blit(text, text_rect)
            else:
                self.shield = False
                self.hammer = False
                self.type = DEFAULT_TYPE

    def athrow_hammer(self):
        self.image_hammer = HAMMER
        if self.hammer:
            self.hammer_rect.x += self.hammer_vel * 8
            self.hammer_vel -= 1

            