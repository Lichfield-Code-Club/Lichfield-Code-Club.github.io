---
Topic:  Club Meeting
Content: Summary
layout: post
author: Mark
---
The following is a simple program where the user has to reach the ! by pressing keys to move up, down, left and right.
It uses the input function which requires the user to press enter. This proves the logic of the game.
The challenge is to replace the input function with something that does not requires the user to press enter, eg keyboard 
https://github.com/boppreh/keyboard#api
Copy and paste the following into Idle and run

from random import randint

maze = [
    ["X","X","X","X",],
    ["X","X","X","X",],
    ["X","X","X","X",],
    ["X","X","X","X",],
    ]
xmax = len(maze[0]) - 1
ymax = len(maze) - 1

def move(xcur,ycur,xpos,ypos):
    done = False
    if xpos >= 0 and xpos <= xmax:
        if ypos >= 0 and ypos <= ymax:
            maze[ycur][xcur] = "X"
            done = maze[ypos][xpos] == '!'
            maze[ypos][xpos] = "?"
    draw()
    return done

def draw():
    for line in maze:
        l = ''
        for xp in line: l += xp
        print(l)

def init():
    x = randint(0,xmax)
    y = randint(0,ymax)
    maze[y][x] = "!"
    xcur = xpos = randint(0,xmax)
    ycur = ypos = randint(0,ymax)
    move(xcur,ycur,xpos,ypos)
    return xcur,ycur

xpos, ypos = xcur,ycur = init()
done = False
while not done:
    newpos = False
    
    print('Next Move')
    key=input()
    
    if key == 'W':
        if ypos < ymax:
            ypos += 1
            newpos = True
    if key == 'S':
        if ypos > 0:
            ypos -= 1
            newpos = True
    if key == 'A':
        if xpos > 0:
            xpos -= 1
            newpos = True
    if key == 'D':
        if xpos < xmax:
            xpos += 1
            newpos = True
    if newpos:
        done = move(xcur,ycur,xpos,ypos)
        xcur = xpos
        ycur = ypos
if done:
    print('Game Over!!')

[boppreh/keyboard](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fboppreh%2Fkeyboard%23api&h=AT0DBVfnWQTC6AFveMl_jKaHklerScxtL7Z4220MHnnGjNZPBPH8NWmhDI-sWi3fhUF53m6Q5IrrXbxoAwOELf9m3p6yFsGL4uadyOTsVRt7CPXUwevG4FPYqdw6y1Xr&s=1)![ALT TEXT](https://external.fbhx4-2.fna.fbcdn.net/emg1/v/t13/10769396810181609814?url=https%3A%2F%2Favatars2.githubusercontent.com%2Fu%2F231856%3Fs%3D400%26v%3D4&fb_obo=1&utld=githubusercontent.com&stp=c0.5000x0.5000f_dst-emg0_p420x420_q75_tt6&edm=AKK4YLsEAAAA&_nc_gid=PPVs8SG5YpiG-h17jw7STA&_nc_oc=Adkqz9gG128oSHDhpjSOSV5d4IiIeV7rmmSVbIBD7yajCNaXPT-fE478bpr1N0r99dQ&ccb=13-1&oh=06_Q3-4AaTtxR6aeYoN98L05HcNCOrCT4cmh79_k5L2P9AwhESj&oe=68F82320&_nc_sid=ef6713)

* [Facebook Link](https://www.facebook.com/720665616418529/posts/2445918752201877)

## Location

* Curborough Community Centre
* WS13 7NY
* Code Club
* Wednesdays 5:30 - 6:30pm
* 7 - 15 year olds welcome

