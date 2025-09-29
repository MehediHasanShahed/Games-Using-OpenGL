from OpenGL.GL import *
from OpenGL.GLUT import *
import random


score = 0
game_state = "playing"  
diamond_pos = [250, 480] 
diamond_color = [random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1)]  
catcher_pos = 250
diamond_speed = 2

def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


    

def midpoint(x1,y1,x2,y2):
    zone = myzone(x1, y1, x2, y2)
    
    x1, y1 = n_to_zero(x1,y1,zone)
    x2, y2 = n_to_zero(x2, y2,zone)
    dx = x2 - x1
    dy = y2 - y1
    dinit = 2 * dy - dx
    dne = 2 * dy - 2 * dx
    de = 2 * dy
    for i in range(int(x1), int(x2)):
        a, b = zero_to_n(x1,y1,zone)
        if dinit >= 0:
            dinit = dinit + dne
            draw_points(a, b)
            x1 += 1
            y1 += 1
        else:
            dinit = dinit + de
            draw_points(a, b)
            x1 += 1

def myzone(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        elif dx > 0 and dy < 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        elif dx > 0 and dy < 0:
            return 6


def zero_to_n(x,y,zone):
    if zone == 0:
        return x,y
    if zone == 1:
        return y,x
    if zone == 2:
        return -y,x
    if zone == 3:
        return -x,y
    if zone == 4:
        return -x,-y
    if zone == 5:
        return -y,-x  
    if zone == 6:
        return y, -x
    if zone == 7:
        return x,-y
    
def n_to_zero(x,y,zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def exit_sign():
    glColor3f(1,0,0)
    midpoint(470, 470, 490, 490)
    midpoint(470, 490, 490, 470)

def pause_sign():
    glColor3f(1,1,0)
    midpoint(245, 470, 245, 490)
    midpoint(255, 470, 255, 490)

def resume_sign():
    glColor3f(1,1,0)
    midpoint(245, 470, 245, 490)
    midpoint(245, 470, 265, 480)
    midpoint(245, 490, 265, 480)

def back_sign():
    glColor3f(0,1,1)
    midpoint(10, 480, 40, 480)
    midpoint(10, 480, 25, 490)
    midpoint(10, 480, 25, 470)



def catcher(color):
    global catcher_pos
    glColor3f(*color)
    midpoint(catcher_pos - 50, 15, catcher_pos + 50, 15)
    midpoint(catcher_pos - 40, 5, catcher_pos + 40, 5)
    midpoint(catcher_pos - 50, 15, catcher_pos - 40, 5)
    midpoint(catcher_pos + 50, 15, catcher_pos + 40, 5)

def diamond():
    global diamond_pos
    glColor3f(*diamond_color)  
    midpoint(diamond_pos[0], diamond_pos[1], diamond_pos[0]-10, diamond_pos[1]+10)
    midpoint(diamond_pos[0], diamond_pos[1], diamond_pos[0]+10, diamond_pos[1]+10)
    midpoint(diamond_pos[0]-10, diamond_pos[1]+10, diamond_pos[0], diamond_pos[1]+20)
    midpoint(diamond_pos[0]+10, diamond_pos[1]+10, diamond_pos[0], diamond_pos[1]+20)



def animate():
    global diamond_pos, diamond_speed, game_state, score, diamond_color
    if game_state == "playing":
        diamond_pos[1] -= diamond_speed
        if diamond_pos[1] < 15: #colission check
            if abs(diamond_pos[0] - catcher_pos) <= 50:  # collidedd
                score += 1
                print("Score:", score)
                diamond_speed += 0.05  
                diamond_pos = [random.randint(20, 480), 480]  
                diamond_color = [random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1)]  
                
            else:
                game_state = "game_over"
                print("Game Over! Score:", score)

        glutPostRedisplay()



def specialKeyListener(key,x,y):
    global catcher_pos
    if game_state == "playing":
        if key == GLUT_KEY_LEFT:
            catcher_pos -= 25
            if catcher_pos < 50:
                catcher_pos = 50
        elif key == GLUT_KEY_RIGHT:
            catcher_pos += 25
            if catcher_pos > 450:
                catcher_pos = 450
        glutPostRedisplay()

def mouseListener(button, state, x, y):
    global game_state, score, diamond_pos, diamond_speed
 
    actualx = x
    actualy = 500 - y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= actualx <= 40 and 470 <= actualy <= 490:      #restart icon
            score = 0
            game_state = "playing"
            diamond_pos = [random.randint(20, 480), 480]
            diamond_speed = 2
            print("Starting Over")
            glutPostRedisplay()
        elif 245 <= actualx <= 265 and 470 <= actualy <= 490:  # resume/pause icon
            if game_state == "playing":
                game_state = "paused"
                print("Game Paused")
            elif game_state == "paused":
                game_state = "playing"
                print("Game Resumed")
            glutPostRedisplay()  
        elif 470 <= actualx <= 490 and 470 <= actualy <= 490:  # Exit icon
            print("Thank you for playing. Your final score:", score)
            glutLeaveMainLoop()


def iterate():
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def showScreen():
    global game_state
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if game_state == "paused":
        resume_sign()  
    else:
        pause_sign()  
    diamond()  
    exit_sign()
    back_sign()
    if game_state == "game_over":
        catcher((1, 0, 0))  #red catcher (game over)
    else:
        catcher((1, 1, 1)) #white catcher
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Game")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()