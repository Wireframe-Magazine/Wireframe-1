import random
import math

# the size of the screen
WIDTH = 800
HEIGHT = 600

# how much a particle slows down by each second
DRAG = 0.8 

# the colour of each particle in R, G, B values
PARTICLE_COLOR = 255, 230, 128

# the time in seconds for which a particle is displayed
MAX_AGE = 3

# an array to hold the details of the explosion particles on the screen
particles = []


# This function creates a new explosion at the specified screen co-ordinates

def explode(x, y, speed=300):

    # these are new particles, so set their age to zero
    age = 0     
    
    # generate 100 particles per explosion
    for _ in range(100):
    
        # for each particle, generate a random angle and distance
        angle = random.uniform (0, 2 * math.pi)
        radius = random.uniform(0, 1) ** 0.5

        # convert angle and distance from the explosion point into x and y velocity for the particle
        vx = speed * radius * math.sin(angle)
        vy = speed * radius * math.cos(angle)
        
        # add the particle's position, velocity and age to the array
        particles.append((x, y, vx, vy, age))


# This function redraws the screen by plotting each particle in the array

def draw():

    # clear the screen
    screen.clear()
    
    # loop through all the particles in the array
    for x, y, *_ in particles:
        
        # for each particle in the array, plot its position on the screen
        screen.surface.set_at((int(x), int(y)), PARTICLE_COLOR)


# This function updates the array of particles

def update(dt):

    # to update the particle array, create a new empty array
    new_particles = []
    
    # loop through the existing particle array
    for (x, y, vx, vy, age) in particles:
    
        # if a particle was created more than a certain time ago, it can be removed
        if age + dt > MAX_AGE:
            continue
            
        # update the particle's velocity - they slow down over time
        drag = DRAG ** dt
        vx *= drag
        vy *= drag
        
        # update the particle's position according to its velocity
        x += vx * dt
        y += vy * dt
        
        # update the particle's age
        age += dt
        
        # add the particle's new position, velocity and age to the new array
        new_particles.append((x, y, vx, vy, age))
        
    # replace the current array with the new one
    particles[:] = new_particles


# This function creates an explosion at a random location on the screen

def explode_random():

    # select a random position on the screen
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    
    # call the explosion function for that position
    explode(x, y)

# call the random explosion function every 1.5 seconds
clock.schedule_interval(explode_random, 1.5)
