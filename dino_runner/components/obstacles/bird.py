import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image):
        #self.type = random.randint(0)
        super().__init__(image, 0)
        self.rect.y = 245