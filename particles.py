# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:20:35 2023

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt

max_vel = 1
max_mass = 1
screen_size = 50
# we assume that size of particle is related to mass, by sqrt
# all collisions are elastic

class particle:
    def __init__(self,mass,velocity,position):
        self.mass = mass
        self.velocity  = velocity
        self.position  = position
    def edge_detect(self):
        if self.position[0]<-screen_size+0.01 or self.position[0]>screen_size-0.01:
            pass
        

def generate_particles(n):
    particles = []
    for i in range(n):
        particles.append(particle(np.random.uniform(0.01,max_mass),
                                  np.random.uniform(-max_vel,max_vel),
                                  np.random.uniform(-screen_size,screen_size,2)))
    return particles

K = generate_particles(10)