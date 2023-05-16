# (C) 2023 TheGoldenMic Media LLC. Code by MrJack TheGoldenMic and DarguzTV

import os
import pygame
import datetime
from enum import Enum

WIN = (600, 600)
BG_IMG = pygame.image.load(os.path.join("assets", "bg.png"))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Platfom:
    PLAT_DIR = Enum('PLAT_DIR', ['STILL', 'UP', 'DOWN'])

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = self.PLAT_DIR.STILL

def draw():
    win.blit(BG_IMG, (0,0))
    pygame.display.update()


if __name__ == "__main__":
    win = pygame.display.set_mode(WIN)
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        draw()

# --------------------------- AI ------------------------

def define_parameters():
    params = dict()
    # Neural Network
    params['epsilon_decay_linear'] = 1/100
    params['learning_rate'] = 0.00013629
    params['first_layer_size'] = 200    # neurons in the first layer
    params['second_layer_size'] = 20   # neurons in the second layer
    params['third_layer_size'] = 50    # neurons in the third layer
    params['episodes'] = 250          
    params['memory_size'] = 2500
    params['batch_size'] = 1000
    # Settings
    params['weights_path'] = 'weights/weights.h5'
    params['train'] = True
    params["test"] = False
    params['plot_score'] = True
    params['log_path'] = 'logs/scores_' + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) +'.txt'
    return params

