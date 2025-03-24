import pgzrun
from random import randint
import pygame

title = "Game Over"
WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

game_over_screen_displayed = False  # New flag to track if animation has been shown

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    if game_over:
        game_over_animation(score)
    else:
        screen.fill("green")
        fox.draw()
        coin.draw()
        screen.draw.text("Score : " + str(score), color='black', topleft=(10, 10))

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if not game_over:
        if keyboard.left:
            fox.x = fox.x - 2
        elif keyboard.right:
            fox.x = fox.x + 2
        elif keyboard.up:
            fox.y = fox.y - 2
        elif keyboard.down:
            fox.y = fox.y + 2

        coin_collected = fox.colliderect(coin)

        if coin_collected:
            score = score + 10
            place_coin()

def game_over_animation(final_score):
    global game_over_screen_displayed
    
    if game_over_screen_displayed:
        return  # If already displayed, do nothing
    
    pygame.init()
    game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Over")
    clock = pygame.time.Clock()
    
    font_large = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 40)
    
    fade_alpha = 0
    
    while fade_alpha < 255:
        game_screen.fill((255, 182, 193))  # Pink background
        game_over_text = font_large.render("GAME OVER", True, (255, 0, 0))  # Red text
        
        game_over_surface = pygame.Surface(game_over_text.get_size(), pygame.SRCALPHA)
        game_over_surface.fill((0, 0, 0, fade_alpha))  # Increasing opacity
        game_over_text.blit(game_over_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        game_screen.blit(game_over_text, (30, 150))
        
        final_score_text = font_small.render(f"Final Score: {final_score}", True, (0, 0, 0))
        game_screen.blit(final_score_text, (100, 250))
        
        pygame.display.flip()
        fade_alpha += 5
        clock.tick(30)
    
    # Display static final screen
    game_screen.fill((255, 182, 193))
    game_over_text = font_large.render("GAME OVER", True, (255, 0, 0))  # Stays large and red
    game_screen.blit(game_over_text, (30, 150))
    
    final_score_text = font_small.render(f"Final Score: {final_score}", True, (0, 0, 0))
    game_screen.blit(final_score_text, (100, 250))
    
    pygame.display.flip()
    
    game_over_screen_displayed = True  # Mark animation as displayed
    
    # Keep displaying the screen without returning to the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        clock.tick(30)

clock.schedule(time_up, 7.0)
place_coin()

pgzrun.go()
