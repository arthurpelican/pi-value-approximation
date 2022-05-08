import pygame
import random as rd
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("press A to add a random point, press Z to add 10, E to add 100, R to add 1000  |   current pi value : 0")
clock = pygame.time.Clock()

WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)

def add_point(win, center, radius, width, height) :
    tmp_point = (rd.random() * width, rd.random() * height)
    tmp_pixel = (int(tmp_point[0]), int(tmp_point[1]))
    pygame.draw.circle(win, RED, (tmp_pixel[0], tmp_pixel[1]), 1)
    distance_to_center = math.sqrt((tmp_point[0] - center[0]) ** 2 + (tmp_point[1] - center[1]) ** 2)
    if distance_to_center <= radius :
        return True
    return False

def main() :
    running = True
    points = set()

    center = (WIDTH // 2, HEIGHT // 2)
    radius = WIDTH // 2

    pi_approximation = 0
    total_points = 0
    points_inside = 0

    WIN.fill(WHITE)

    pygame.draw.circle(WIN, BLACK, center, WIDTH // 2)
    pygame.draw.circle(WIN, WHITE, center, WIDTH // 2 - 2)

    while running :
        clock.tick(FPS)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                break
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] :
            inside_circle = add_point(WIN, center, radius, WIDTH, HEIGHT)
            total_points += 1
            if inside_circle :
                points_inside += 1

        elif keys[pygame.K_z] :
            for _ in range(10) : 
                inside_circle = add_point(WIN, center, radius, WIDTH, HEIGHT)
                total_points += 1
                if inside_circle :
                    points_inside += 1
    
        elif keys[pygame.K_e] :
            for _ in range(100) : 
                inside_circle = add_point(WIN, center, radius, WIDTH, HEIGHT)
                total_points += 1
                if inside_circle :
                    points_inside += 1
        elif keys[pygame.K_r] :
            for _ in range(1000) : 
                inside_circle = add_point(WIN, center, radius, WIDTH, HEIGHT)
                total_points += 1
                if inside_circle :
                    points_inside += 1
        
        if total_points > 0 :
            pi_approximation = points_inside / total_points * 4

        pygame.display.set_caption(f"press A to add a random point, press Z to add 10, E to add 100  |  current pi value : {str(pi_approximation)[0:8]}  |  {points_inside} points inside the circle out of {total_points}")

        pygame.display.update()

if __name__ == "__main__" :
    main()
