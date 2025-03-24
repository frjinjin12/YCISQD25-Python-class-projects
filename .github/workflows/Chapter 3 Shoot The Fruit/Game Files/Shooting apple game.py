import pgzrun
from random import randint

# Set screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize game variables
score = 0
game_over = False

# Create apple actor
apple = Actor("apple")

# Function to place the apple fully inside the screen
def place_apple():
    apple.x = randint(apple.width // 2, WIDTH - apple.width // 2)
    apple.y = randint(apple.height // 2, HEIGHT - apple.height // 2)

# Function to draw the screen
def draw():
    screen.fill((50, 150, 255))  # Change background color

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10,10),fontsize=60)
    else:
        apple.draw()
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="black")  # Scoreboard

# Function to check mouse click
def on_mouse_down(pos):
    global score, game_over

    if not game_over:  # Only check clicks if the game is running
        if apple.collidepoint(pos):
            print("YEY! You hit the apple!")
            score += 1
            place_apple()  # Move the apple to a new position
        else:
            print("Missed!")
            game_over = True  # End the game if the player misses

# Place the first apple
place_apple()

# Run the game
pgzrun.go()
