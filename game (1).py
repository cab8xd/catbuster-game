# Game Psuedocode - Christine Baca cab8xd & Brooke Bonfadini brb3mt

# Game will be ghost buster themed. The player will be trying to survive in a haunted house for a certain period of time.



# Required Mechanics:
#   User input:
#       Player should be able to move up/down/possibly jump and shoot
#   Graphics/Images:
#       The theme will be a haunted house. The enemies will be ghosts and spooky things.
#   Start screen:
#       A start screen will be included in the code. The user must click enter to start the game.
#   Window size:
#       Window size will be 800 by 600 units

# Optional Features:
#   Animation:
#      The player and possibly the enemies will be animated sprites. The player will look like they're running with the moving camera
#   Enemies:
#       There will ghost enemies that will come towards the player. The only way to deter the ghosts will be for the player to shoot them.
#   Scrolling Level:
#       The game will scroll in the positive x direction along with the player's automatic movement
#   Timer:
#       There will be a countdown. The score will be depend on how long the player survives or whether they reach the end of the countdown.
#   Health Meter:
#       Every time an enemy touches the player will lose one health point. The player will have 3 health points to begin the game

import pygame
import gamebox
import random
camera = gamebox.Camera(800, 600)
sheet = gamebox.load_sprite_sheet(
  "small_cat.png",
  1,4)
sheet = [
    # movement key:
        #sheet[0] # leg mid, front
        #sheet[1] # outstretch
        #sheet[2] #close
        #sheet[3] #outstretch, leg front
    sheet[3],
    sheet[0],
    sheet[2],
    sheet[1],
    sheet[0],
    sheet[2]
]

player = gamebox.from_image(camera.x, camera.y, sheet[0])
pipes = []
counter = 0
time = 3600
score = 0
player.cool_down = 0
obstacles = [
    gamebox.from_color(200, 400, 'green', 400, 20),
    gamebox.from_color(100, 200, 'white', 100, 10),
]
special = [
    gamebox.from_color(300, 300, 'red', 30, 150),
]
bullets = [
    gamebox.from_image(-300, 300, 'bullet2.png'),
]
ticks = 0
enemies = []
hp = 3
x = 0
enemies_remove = []
border_top = gamebox.from_color(400, 20, 'lightblue', 850, 50)
bottom_border = gamebox.from_color(400, 580, "lightblue", 850, 50)
game1 = True
background = gamebox.from_image(400, 300, 'wood.png') #add background every 850 pixels horizontally
background2 = gamebox.from_image(1250, 300, 'wood.png')
background3 = gamebox.from_image(2100, 300, 'wood.png')


#bullet link: http://img3.wikia.nocookie.net/__cb20120731090012/commando2/images/thumb/8/84/Glenos-G_160_bullet.png/500px-Glenos-G_160_bullet.png

def tick(keys):
    global counter
    global time, score
    global ticks
    global hp
    global x
    global game1
    if game1:
        if pygame.K_RETURN not in keys:
            camera.clear('black')
            welcome = gamebox.from_text(camera.x, camera.y - 100, "Welcome to Catastrophe", 40, 'white')
            instructions = gamebox.from_text(camera.x, camera.y - 50, "Your goal is to survive for about 1 minute in a haunted house filled with ghosts", 30, 'white')
            instructions2 = gamebox.from_text(camera.x, camera.y, "Use the arrow keys to move and the space bar to shoot at the ghosts", 30, 'white')
            instructions3 = gamebox.from_text(camera.x, camera.y + 50, "Be sure to avoid walls and eliminate ghosts before they reach you", 30, 'white')
            begin = gamebox.from_text(camera.x, camera.y + 100, "You have 3 lives. PRESS THE ENTER KEY TO BEGIN!", 30, 'white')
            camera.draw(welcome)
            camera.draw(instructions)
            camera.draw(instructions2)
            camera.draw(instructions3)
            camera.draw(begin)
            camera.display()
            return
        game1 = False
    x += 1
    camera.draw(background)
    camera.draw(background2)
    if background.x < camera.x - 850:
        background.x += 1700
    if background2.x < camera.x - 850:
        background2.x += 1700
    camera.x += 3
    if pygame.K_UP in keys:
        player.y -= 10
    if pygame.K_DOWN in keys:
        player.y += 10
    player.y = player.y + player.yspeed
    player.x = player.x + player.xspeed
    player.xspeed = 3
    camera.draw(player)
    counter += 1
    ticks += 1
    if counter % 20 ==0:
        score +=1
    time -= 1
    seconds = str(int((time / 60))).zfill(3)
    if seconds == str('000'):
        win_box = gamebox.from_text(camera.x, 200, "YOU WON!", 100, "white")
        end_background = gamebox.from_color(camera.x, 300, 'black', 800, 600)
        camera.draw(end_background)
        camera.draw(win_box)
        camera.display()
        gamebox.pause()
        return
    if counter % 50 == 0:
        new_pipe_top = gamebox.from_color(camera.x + 400, 0, "white", 40, random.randint(0, 500))
        new_pipe_bottom = gamebox.from_color(camera.x + 400, 600, "white", 40, random.randint(0, 500))
        pipes.append(new_pipe_top)
        pipes.append(new_pipe_bottom)
    for pipe in pipes:
        if pipe.x < camera.x - 450:
            pipes.remove(pipe)
        if player.touches(pipe, -40, 10):
            end_box = gamebox.from_text(camera.x, 200, "GAME OVER", 100, "white")
            end_score = gamebox.from_text(camera.x, 350, "Score: " + str(score), 100, "white")
            end_background = gamebox.from_color(camera.x, 300, 'black', 800, 600)
            camera.draw(end_background)
            camera.draw(end_box)
            camera.draw(end_score)
            camera.display()
            gamebox.pause()
            return
        camera.draw(pipe)
    if player.y > camera.y + 700 or player.x > camera.x + 500 or player.x < camera.x - 450 or player.y < 0:
        end_box = gamebox.from_text(camera.x, 200, "GAME OVER", 100, "white")
        end_score = gamebox.from_text(camera.x, 350, "Score: " + str(score), 100, "white")
        end_background = gamebox.from_color(camera.x, 300, 'black', 800, 600)
        camera.draw(end_background)
        camera.draw(end_box)
        camera.draw(end_score)
        camera.display()
        gamebox.pause()
        return
    for bullet in bullets:
        bullet.move_speed()
    if pygame.K_LEFT in keys:
        player.x -= 10
    if pygame.K_RIGHT in keys:
        player.x += 10
    if pygame.K_UP in keys:
        for obs in obstacles + special:
            if player.bottom_touches(obs):
                player.speedy = -20
    if pygame.K_SPACE in keys:
        bullets.append(
            gamebox.from_image(-300, 300, 'bullet2.png'),
        )
        bullets[-1].speedx = 10
        bullets[-1].center = player.center
        keys.remove(pygame.K_SPACE)

    for obs in obstacles:
        player.move_to_stop_overlapping(obs)
    for obs in special:
        obs.move_to_stop_overlapping(player)
        for ob2 in obstacles:
            obs.move_to_stop_overlapping(ob2)

    camera.draw(player)
    for obs in bullets:
        camera.draw(obs)
    #start of code for enemies
    if counter % 100 == 0:
        new_enemy = gamebox.from_color(50,random.randrange(0,600),"blue",50,50)
        enemies.append(new_enemy)
    for count in range(len(enemies)):
        sheet_enemies = gamebox.load_sprite_sheet(
            "spooks.png",
            9, 9)
        sheet_enemies = [
            sheet_enemies[1],
            sheet_enemies[2],
            sheet_enemies[3],
            sheet_enemies[4],
        ]
        if player.x < enemies[count].x:
            enemies[count].x -= 1 * ((ticks % 20) - 5)
        else:
            enemies[count].x -= 2
        enemies[count].speedy += random.randrange(-5, 6) * 0.1
        enemies[count].move_speed()
        if enemies[count].right < camera.left:
            enemies[count].left = camera.right
        if enemies[count].left > camera.right:
            enemies[count].right = camera.left
        enemies[count].image = sheet_enemies[(ticks // 5) % len(sheet_enemies)]
        camera.draw(enemies[count])
        camera.draw(player)
    for enemy in enemies:
        if enemy.x < camera.x - 450:
            enemies_remove.append(enemy)
        if player.touches(enemy, -40, 10) and x > 80:
            hp -= 1
            x = 0
        if hp == 0:
            end_box = gamebox.from_text(camera.x, 200, "GAME OVER", 100, "white")
            end_score = gamebox.from_text(camera.x, 350, "Score: "+str(score),100, "white")
            end_background = gamebox.from_color(camera.x, 300, 'black', 800, 600)
            camera.draw(end_background)
            camera.draw(end_box)
            camera.draw(end_score)
            camera.display()
            gamebox.pause()
            return
    for enemy in enemies_remove:
        enemies.remove(enemy)
    for enemy in enemies:
        for bullet in bullets:
            if bullet.touches(enemy):
                enemies.remove(enemy)
    camera.draw(border_top)
    border_top.x += 3
    camera.draw(bottom_border)
    bottom_border.x += 3
    health_box = gamebox.from_text(camera.x - 200, 30, "Lives: " + str(hp), 24, 'darkblue')
    time_box = gamebox.from_text(camera.x + 100, 30, "Time Left for Survival: " + seconds, 24, "white")
    score_box = gamebox.from_text(camera.x - 100, 30, "Score: " + str(score), 24, "white")
    camera.draw(time_box)
    camera.draw(score_box)
    camera.draw(health_box)
    player.image = sheet[(ticks // 6) % len(sheet)]
    camera.draw(player)
    camera.display()

gamebox.timer_loop(60, tick)