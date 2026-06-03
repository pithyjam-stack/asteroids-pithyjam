import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    print("Displaying screen...")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting clock...")
    clock = pygame.time.Clock()
    dt: float = 0.0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    print("Instantiating player...")
    player = Player(x, y)

    while True:
        log_state()
        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
