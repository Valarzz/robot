from env_map import grid
from sklearn.preprocessing import normalize
import numpy as np


class robot:
    def __init__(self, init_x, init_y, speed):
        self.x = init_x
        self.y = init_y
        self.speed = speed

    def move(self, des):
        n = des - np.array([self.x, self.y])
        self.d = normalize(n[:, np.newaxis], axis=0).ravel() * self.speed
        self.x += self.d[0]
        self.y += self.d[1]

