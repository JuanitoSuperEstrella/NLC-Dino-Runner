import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.cactus = [SMALL_CACTUS, LARGE_CACTUS]
        self.obstacles = []
        
    def update(self, game):
        self.num_ran = random.randint(0,1)
        if len(self.obstacles) == 0:
            small_cactus = Cactus(self.cactus[self.num_ran])
            self.obstacles.append(small_cactus)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []