from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import math

shooter = [250, 40]
bulletcenter = [0, -math.inf]
bulletstate = False
bulletmiss = 0
fiveopponents = [[],[],[],[],[]]
score=0
game_state = 'Playing'
missed_count  = 0

fiveopponents[0] = [random.randint(30, 70), 440, random.randint(15, 30)]  #[x,y,r]
fiveopponents[1] = [random.randint(130, 170), 440, random.randint(15, 30)]
fiveopponents[2] = [random.randint(230, 270), 440, random.randint(15, 30)]
fiveopponents[3] = [random.randint(330, 370), 440, random.randint(15, 30)]
fiveopponents[4] = [random.randint(430, 470), 440, random.randint(15, 30)]
opponentarea = [[], [], [], [], []]


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def midpoint_circle(cx, cy, r):
    d = 1 - r
    x = 0
    y = r
    draw_points(x + cx, y + cy)
    draw_points(-x + cx, y + cy)
    draw_points(-y + cx, x + cy)
    draw_points(-y + cx, -x + cy)
    draw_points(-x + cx, -y + cy)
    draw_points(x + cx, -y + cy)
    draw_points(y + cx, -x + cy)
    draw_points(y + cx, x + cy)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3 # e
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5  #se
            x += 1
            y -= 1
        draw_points(x + cx, y + cy)
        draw_points(-x + cx, y + cy)
        draw_points(-y + cx, x + cy)
        draw_points(-y + cx, -x + cy)
        draw_points(-x + cx, -y + cy)
        draw_points(x + cx, -y + cy)
        draw_points(y + cx, -x + cy)
        draw_points(y + cx, x + cy)

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
    glColor3f(1,0.75,0)
    midpoint(245, 470, 245, 490)
    midpoint(255, 470, 255, 490)

def resume_sign():
    glColor3f(1,0.75,0)
    midpoint(245, 470, 245, 490)
    midpoint(245, 470, 265, 480)
    midpoint(245, 490, 265, 480)

def back_sign():
    glColor3f(0,1,1)
    midpoint(10, 480, 40, 480)
    midpoint(10, 480, 25, 490)
    midpoint(10, 480, 25, 470)


def bulletshooter(gameover=False):
    global shooter
    if gameover == True:
      glColor3f(1,0,0)
    else:
      glColor3f(0,0.6,1)

    midpoint_circle(shooter[0], shooter[1], 15)


def bullet():
    global shooter

    glColor3f(1,1,1)
    midpoint_circle(bulletcenter[0], bulletcenter[1], 5)




def keyboardListener(key, x, y):
    global bulletstate, bulletcenter, shooter, shooter,game_state
    if key==b' ' and game_state == 'Playing' and bulletstate != True:
        bulletcenter[0], bulletcenter[1] = shooter[0], shooter[1] + 20
        bulletstate = True
    
    if key == b'a' and game_state == 'Playing':
        shooter[0] -= 15
        if shooter[0] < 15:
            shooter[0] = 15
    elif key == b'd' and game_state == 'Playing':
        shooter[0] += 15
        if shooter[0] > 485:
            shooter[0] = 485

    glutPostRedisplay()


def mouseListener(button, state, x, y):
    global game_state, score,fiveopponents,shooter,bulletcenter,bulletstate,opponentarea,missed_count,bulletmiss
    actualx = x
    actualy = 500 - y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= actualx <= 40 and 470 <= actualy <= 490:      #restart icon
            shooter = [250, 40]
            bulletcenter = [0, -math.inf]
            bulletstate = False
            fiveopponents = [[],[],[],[],[]]
            score=0
            missed_count=0
            bulletmiss = 0
            game_state = 'Playing'
           
            fiveopponents[0] = [random.randint(30, 70), 440, random.randint(15, 30)]
            fiveopponents[1] = [random.randint(130, 170), 440, random.randint(15, 30)]
            fiveopponents[2] = [random.randint(230, 270), 440, random.randint(15, 30)]
            fiveopponents[3] = [random.randint(330, 370), 440, random.randint(15, 30)]
            fiveopponents[4] = [random.randint(430, 470), 440, random.randint(15, 30)]
            opponentarea = [[], [], [], [], []]

            print("Starting Over")
            glutPostRedisplay()
        elif 245 <= actualx <= 265 and 470 <= actualy <= 490:  # resume/pause icon
            if game_state == "Playing":
                game_state = "Paused"
                print("Game Paused")
            elif game_state == "Paused":
                game_state = "Playing"
                print("Game Resumed")
            glutPostRedisplay()  
        elif 470 <= actualx <= 490 and 470 <= actualy <= 490:  # Exit icon
            print("Thank you for playing. Your final score:", score)
            glutLeaveMainLoop()

def checkcolission():
    global bulletcenter, shooter, fiveopponents, opponentarea
    for i in range(len(opponentarea)):
        
        if opponentarea[i][0] <= bulletcenter[0] <= opponentarea[i][1] and opponentarea[i][2] <= bulletcenter[1] <= opponentarea[i][3]:
            return i
    return -1

def checkclash():
    global shooter, opponentarea
    for i in range(len(opponentarea)):     # opponent area parameters x-r,x+r,y-r,y+r
        if opponentarea[i][0] <= shooter[0] - 15  <= opponentarea[i][1] and opponentarea[i][2] <= shooter[1] <= opponentarea[i][3]:
            return True                          #bulletshooter radius 15
        if opponentarea[i][0] <= shooter[0] + 15 <= opponentarea[i][1] and opponentarea[i][2] <= shooter[1] <= opponentarea[i][3]:
            return True
        if opponentarea[i][0] <= shooter[0] <= opponentarea[i][1] and opponentarea[i][2] <= shooter[1] + 15 <= opponentarea[i][3]:
            return True
    return False
        
def animate():
    global bulletcenter, shooter, fiveopponents, opponentarea,bulletstate,score,game_state,missed_count,bulletmiss

    if game_state == 'Playing':
        bulletcenter[1] += 40
        for i in range(len(fiveopponents)):
            fiveopponents[i][1] -= 0.5       #missed the opponents
            if fiveopponents[i][1]<=15:
                missed_count += 1
                fiveopponents[i] = [random.randint(30,470),440,random.randint(15,30)]
                print("Missed: ",missed_count,'Life Remaining',3-missed_count)
                if missed_count == 3:
                    game_state = 'Game Over'
                    print('Game Over. Final Score: ',score)
            opponentarea[i] = [fiveopponents[i][0] - fiveopponents[i][2], fiveopponents[i][0] + fiveopponents[i][2],fiveopponents[i][1] - fiveopponents[i][2],fiveopponents[i][1] + fiveopponents[i][2]]  
             # area parameters x-r,x+r,y-r,y+r     opponentarea = [[x-r,x+r,y-r,y+r],[x-r,x+r,y-r,y+r],...]

        
        import math
        if bulletcenter[1]>500:
            bulletmiss += 1                               # missed bullet
            print('Bullet missed: ',bulletmiss,)
            if bulletmiss == 3:
                game_state = 'Game Over'        
            bulletcenter[1]= -math.inf
            bulletstate = False

        clash = checkclash()
        if clash == True:
            game_state = "Game Over"                #direct clash
            print('Game Over. Final Score: ',score)
            
        idx = checkcolission()
        if idx != -1:
            fiveopponents[idx]=[random.randint(30,470),440,random.randint(15,30)]        #scored
            bulletstate=False    
            bulletcenter=[0,-math.inf]
            score += 1
            print("SCORE: ",score)
        
    glutPostRedisplay()


def showScreen():
    global bulletstate, bulletcenter, shooter,game_state,opponentarea
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if game_state == 'Game Over':
        bulletshooter(True)
    else:
        bulletshooter()

    if bulletstate == True:
        bullet()
    for i in fiveopponents:
        glColor3f(1,1,1)
        midpoint_circle(i[0], i[1], i[2])

    if game_state == "Paused":
        resume_sign()  
    else:
        pause_sign()  
   
    exit_sign()
    back_sign()
    
    glutSwapBuffers()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Game")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)


glutMainLoop()