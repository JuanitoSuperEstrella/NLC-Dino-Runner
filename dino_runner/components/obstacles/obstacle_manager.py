import pygame
import random

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.cactus = [SMALL_CACTUS, LARGE_CACTUS]
        self.obstacles = []
        self.dinosaur = Dinosaur()
        
    def update(self, game):
        self.num_ran = random.randint(0,1)
        if len(self.obstacles) == 0:
            bird = Bird(BIRD)
            small_cactus = Cactus(self.cactus[self.num_ran])
            obstacles_ = [bird, small_cactus]
            self.obstacles.append(obstacles_[self.num_ran])
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                else:

                    self.obstacles.remove(obstacle)
            
            break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []