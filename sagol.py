import pygame
import sys
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (52, 152, 219)
DARK_BLUE = (41, 128, 185)
GRAY = (44, 62, 80)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing in Spinning Hexagon")
clock = pygame.time.Clock()

# Simulation parameters
gravity = 0.2
friction = 0.02
rotation_speed = 0.05
restitution = 0.8  # Bounciness coefficient

# Hexagon properties
hexagon_radius = 200
hexagon_rotation = 0
hexagon_points = []

# Ball properties
ball = {
    "x": 0,
    "y": -hexagon_radius * 0.6,
    "radius": 15,
    "vx": 2,
    "vy": 0,
    "color": BLUE,
    "outline": DARK_BLUE
}

# Initialize hexagon points
for i in range(6):
    angle = (i * math.pi / 3) + math.pi / 6
    hexagon_points.append({
        "x": math.cos(angle) * hexagon_radius,
        "y": math.sin(angle) * hexagon_radius
    })

def get_rotated_hexagon():
    """Return hexagon points rotated by current rotation angle"""
    rotated = []
    cos = math.cos(hexagon_rotation)
    sin = math.sin(hexagon_rotation)
    
    for point in hexagon_points:
        rotated.append({
            "x": point["x"] * cos - point["y"] * sin,
            "y": point["x"] * sin + point["y"] * cos
        })
    
    return rotated

def find_intersection(p1, p2, ball_pos, ball_radius):
    """Find intersection between ball path and hexagon edge"""
    dx = p2["x"] - p1["x"]
    dy = p2["y"] - p1["y"]
    length = math.sqrt(dx**2 + dy**2)
    
    if length == 0:
        return None
    
    nx = -dy / length
    ny = dx / length
    
    dist = (ball_pos["x"] - p1["x"]) * nx + (ball_pos["y"] - p1["y"]) * ny
    
    if abs(dist) < ball_radius:
        closest_x = ball_pos["x"] - dist * nx
        closest_y = ball_pos["y"] - dist * ny
        
        # Check if closest point is within the segment
        dot = ((closest_x - p1["x"]) * dx + (closest_y - p1["y"]) * dy) / (length**2)
        
        if 0 <= dot <= 1:
            return {
                "x": closest_x,
                "y": closest_y,
                "normal_x": nx,
                "normal_y": ny,
                "penetration": ball_radius - abs(dist)
            }
    
    return None

def reset_simulation():
    """Reset the simulation to initial state"""
    global hexagon_rotation
    ball["x"] = 0
    ball["y"] = -hexagon_radius * 0.6
    ball["vx"] = 2 + 2 * (0.5 - (pygame.time.get_ticks() % 1000) / 1000)
    ball["vy"] = 0
    hexagon_rotation = 0

def update_simulation():
    """Update physics simulation"""
    global hexagon_rotation
    
    # Apply gravity
    ball["vy"] += gravity
    
    # Apply friction
    ball["vx"] *= (1 - friction)
    ball["vy"] *= (1 - friction)
    
    # Update position
    ball["x"] += ball["vx"]
    ball["y"] += ball["vy"]
    
    # Get rotated hexagon
    rotated_hexagon = get_rotated_hexagon()
    
    # Check collision with hexagon edges
    for i in range(6):
        p1 = rotated_hexagon[i]
        p2 = rotated_hexagon[(i + 1) % 6]
        
        intersection = find_intersection(p1, p2, ball, ball["radius"])
        
        if intersection:
            # Calculate wall velocity due to rotation
            angular_velocity = rotation_speed
            wall_vel_x = -intersection["y"] * angular_velocity
            wall_vel_y = intersection["x"] * angular_velocity
            
            # Calculate relative velocity
            rel_vel_x = ball["vx"] - wall_vel_x
            rel_vel_y = ball["vy"] - wall_vel_y
            
            # Calculate dot product with normal
            dot_product = rel_vel_x * intersection["normal_x"] + rel_vel_y * intersection["normal_y"]
            
            # Only bounce if moving toward the wall
            if dot_product < 0:
                # Calculate impulse (bounce)
                j = -(1 + restitution) * dot_product
                
                # Apply impulse
                ball["vx"] += j * intersection["normal_x"]
                ball["vy"] += j * intersection["normal_y"]
                
                # Add wall velocity back
                ball["vx"] += wall_vel_x
                ball["vy"] += wall_vel_y
                
                # Position correction to prevent sticking
                ball["x"] += intersection["normal_x"] * intersection["penetration"] * 1.1
                ball["y"] += intersection["normal_y"] * intersection["penetration"] * 1.1
    
    # Rotate hexagon
    hexagon_rotation += rotation_speed
    
    # Keep rotation between 0 and 2π
    if hexagon_rotation > math.pi * 2:
        hexagon_rotation -= math.pi * 2
    if hexagon_rotation < 0:
        hexagon_rotation += math.pi * 2

def draw_simulation():
    """Draw everything on screen"""
    screen.fill(WHITE)
    
    # Center coordinate system
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    
    # Draw hexagon
    rotated_hexagon = get_rotated_hexagon()
    points = []
    for point in rotated_hexagon:
        points.append((center_x + point["x"], center_y + point["y"]))
    
    pygame.draw.polygon(screen, GRAY, points, 3)
    
    # Draw ball
    pygame.draw.circle(
        screen, 
        ball["color"], 
        (int(center_x + ball["x"]), int(center_y + ball["y"])), 
        ball["radius"]
    )
    pygame.draw.circle(
        screen, 
        ball["outline"], 
        (int(center_x + ball["x"]), int(center_y + ball["y"])), 
        ball["radius"], 
        2
    )
    
    # Draw UI
    font = pygame.font.SysFont('Arial', 16)
    gravity_text = font.render(f"Gravity: {gravity:.2f}", True, BLACK)
    friction_text = font.render(f"Friction: {friction:.2f}", True, BLACK)
    rotation_text = font.render(f"Rotation Speed: {rotation_speed:.2f}", True, BLACK)
    controls_text = font.render("R: Reset  Q: Quit", True, BLACK)
    
    screen.blit(gravity_text, (10, 10))
    screen.blit(friction_text, (10, 30))
    screen.blit(rotation_text, (10, 50))
    screen.blit(controls_text, (10, 80))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_q:
                running = False
            elif event.key == K_r:
                reset_simulation()
    
    # Update simulation
    update_simulation()
    
    # Draw everything
    draw_simulation()
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

