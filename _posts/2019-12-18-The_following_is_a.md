---
Date:   2019-12-18
Topic:  Club Meeting
Content: Summary
---
[<img width="420px" height="420" src="https://external.fbhx6-1.fna.fbcdn.net/emg1/v/t13/10769396810181609814?url=https%3A%2F%2Favatars2.githubusercontent.com%2Fu%2F231856%3Fs%3D400%26v%3D4&fb_obo=1&utld=githubusercontent.com&stp=c0.5000x0.5000f_dst-emg0_p420x420_q75&ccb=13-1&oh=06_AbGSiosjIt0nibBxOQd12YtgptHVAvw40-sYJLU74NmlaA&oe=65288D20&_nc_sid=e609ca/>"](https://external.fbhx6-1.fna.fbcdn.net/emg1/v/t13/10769396810181609814?url=https%3A%2F%2Favatars2.githubusercontent.com%2Fu%2F231856%3Fs%3D400%26v%3D4&fb_obo=1&utld=githubusercontent.com&stp=c0.5000x0.5000f_dst-emg0_p420x420_q75&ccb=13-1&oh=06_AbGSiosjIt0nibBxOQd12YtgptHVAvw40-sYJLU74NmlaA&oe=65288D20&_nc_sid=e609ca)

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

* [Facebook Link](https://www.facebook.com/1481985248595237/posts/2445918752201877/)

## Location

* Curborough Community Centre
* WS13 7NY
* Code Club
* Wednesdays 5:30 - 6:30pm
* 7 - 15 year olds welcome

## Club Links

* [Code Club Website](https://lichfield-code-club.github.io/)
* [Facebook Page](https://www.facebook.com/LichfieldCoders)
* [Discord club messages](https://discord.gg/szz6xGK)
