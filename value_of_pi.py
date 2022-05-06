from unittest import runner
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

def add_point(e,  width, height) :
    tmp_point = (rd.random() * width, rd.random() * height)
    e.add(tmp_point)
    return tmp_point

def verify_point(point, center, radius) :
    distance_to_center = math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)
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

    while running :
        clock.tick(FPS)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                break
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] :
            new_point = add_point(points, WIDTH, HEIGHT)
            total_points += 1

            inside_circle = verify_point(new_point, center, radius)
            if inside_circle :
                points_inside += 1
        elif keys[pygame.K_z] :
            for _ in range(10) : 
                new_point = add_point(points, WIDTH, HEIGHT)
                total_points += 1

                inside_circle = verify_point(new_point, center, radius)
                if inside_circle :
                    points_inside += 1
    
        elif keys[pygame.K_e] :
            for _ in range(100) : 
                new_point = add_point(points, WIDTH, HEIGHT)
                total_points += 1

                inside_circle = verify_point(new_point, center, radius)
                if inside_circle :
                    points_inside += 1
        elif keys[pygame.K_r] :
            for _ in range(1000) : 
                new_point = add_point(points, WIDTH, HEIGHT)
                total_points += 1

                inside_circle = verify_point(new_point, center, radius)
                if inside_circle :
                    points_inside += 1

        WIN.fill(WHITE)

        pygame.draw.circle(WIN, BLACK, center, WIDTH // 2)
        pygame.draw.circle(WIN, WHITE, center, WIDTH // 2 - 2)

        for point in points :
            x = point[0]
            y = point[1]

            pygame.draw.circle(WIN, RED, (int(x), int(y)), 1)
        
        if total_points > 0 :
            pi_approximation = points_inside / total_points * 4

        pygame.display.set_caption(f"press A to add a random point, press Z to add 10, E to add 100  |  current pi value : {pi_approximation}  |  {points_inside} points inside the circle out of {total_points}")

        pygame.display.update()

if __name__ == "__main__" :
    main()