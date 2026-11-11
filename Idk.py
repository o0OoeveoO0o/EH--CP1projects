import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic Physics Starter")
clock = pygame.time.Clock()

# Colors
SKY_BLUE = (100, 180, 255)
GROUND_GREEN = (34, 177, 76)
CHECKER_BROWN = (136, 80, 40)
SONIC_BLUE = (0, 102, 204)
SPIN_BLUE = (30, 144, 255)

# Physics Constants
ACCEL = 0.35          # How fast Sonic builds speed
FRICTION = 0.25       # How fast Sonic slows down when no keys are pressed
DECEL = 0.75          # Skidding speed when turning around while moving fast
MAX_SPEED = 14.0      # Top running speed
GRAVITY = 0.65        # Downward pull
JUMP_FORCE = -13.5    # Initial upward jump velocity
GROUND_Y = 360        # Floor height

# Player State
player_x = 100.0
player_y = float(GROUND_Y)
vx = 0.0
vy = 0.0
on_ground = True
is_spinning = False
radius = 20

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Jump input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                vy = JUMP_FORCE
                on_ground = False
                is_spinning = True

    # Horizontal Movement & Momentum
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if vx > 0:
            vx -= DECEL  # Skidding to a stop
        elif vx > -MAX_SPEED:
            vx -= ACCEL  # Accelerating left
    elif keys[pygame.K_RIGHT]:
        if vx < 0:
            vx += DECEL  # Skidding to a stop
        elif vx < MAX_SPEED:
            vx += ACCEL  # Accelerating right
    else:
        # Apply friction when no directional keys are held
        if abs(vx) < FRICTION:
            vx = 0.0
        elif vx > 0:
            vx -= FRICTION
        elif vx < 0:
            vx += FRICTION

    # Apply Gravity
    if not on_ground:
        vy += GRAVITY

    # Update Position
    player_x += vx
    player_y += vy

    # Screen Wrap-around (for endless running)
    if player_x > WIDTH + radius:
        player_x = -radius
    elif player_x < -radius:
        player_x = WIDTH + radius

    # Ground Collision
    if player_y >= GROUND_Y:
        player_y = float(GROUND_Y)
        vy = 0.0
        on_ground = True
        is_spinning = False

    # Drawing
    screen.fill(SKY_BLUE)
    
    # Draw Green Hill style ground
    pygame.draw.rect(screen, CHECKER_BROWN, (0, GROUND_Y + radius, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.rect(screen, GROUND_GREEN, (0, GROUND_Y + radius, WIDTH, 15))

    # Draw Player (Spinning ball vs standing)
    color = SPIN_BLUE if is_spinning else SONIC_BLUE
    pygame.draw.circle(screen, color, (int(player_x), int(player_y)), radius)

    pygame.display.flip()
    clock.tick(60)
