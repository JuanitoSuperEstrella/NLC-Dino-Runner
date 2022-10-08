import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self,points):
        shield = Shield()
        hammer = Hammer()
        self.powers = [shield, hammer]
        num_ran = random.randint(0, 1)
        self.power = self.powers[num_ran]
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                self.when_appears = random.randint(self.when_appears * 100, self.when_appears * 200)
                self.power_ups.append(self.power)

    def update(self, points, game_speed, player ):
        self.generate_power_up(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.hammer = True
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(5,8)
                player.shield_time_up = power_up.start_time + (time_random * 1000 )
                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = [] 
        self.when_appears = random.randint(50, 150)
