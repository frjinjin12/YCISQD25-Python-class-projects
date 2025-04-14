from random import randint
import pgzrun
import time

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0
start_time = 0
end_time = 0
game_over = False

# Generate non-overlapping dots
while len(dots) < 10:
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    # Check for overlap
    if not any(existing.distance_to(actor) < 30 for existing in dots):
        dots.append(actor)

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0] - 10, dot.pos[1] + 12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

    if game_over:
        total_time = round(end_time - start_time, 2)
        screen.draw.text(f"Time: {total_time}s", (WIDTH // 2 - 50, HEIGHT // 2 - 20), fontsize=40, color="white")
        screen.draw.text("Press R to Retry", (WIDTH // 2 - 70, HEIGHT // 2 + 20), fontsize=30, color="white")

def on_mouse_down(pos):
    global next_dot, lines, start_time, end_time, game_over

    if game_over:
        return

    if next_dot == 0:
        start_time = time.time()

    if next_dot < len(dots) and dots[next_dot].collidepoint(pos):
        if next_dot > 0:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1

        if next_dot == len(dots):
            end_time = time.time()
            game_over = True
    else:
        lines = []
        next_dot = 0
        start_time = 0

def on_key_down(key):
    global dots, lines, next_dot, start_time, end_time, game_over
    if key == keys.R and game_over:
        # Reset game
        dots = []
        lines = []
        next_dot = 0
        start_time = 0
        end_time = 0
        game_over = False

        # Generate non-overlapping dots again
        while len(dots) < 10:
            actor = Actor("dot")
            actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
            if not any(existing.distance_to(actor) < 30 for existing in dots):
                dots.append(actor)

pgzrun.go()
