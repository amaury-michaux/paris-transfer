import sys
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
FPS=60

COLOR_BG = (34, 139, 34)     
COLOR_ROAD = (50, 50, 50)    
COLOR_LINE = (255, 255, 255)   
COLOR_CAR = (220, 20, 60)     

ROAD_WIDTH=300
ROAD_X=(SCREEN_WIDTH-ROAD_WIDTH)//2

CAR_WIDTH=40
CAR_HEIGHT=70

INITIAL_CAR_X=ROAD_X+(ROAD_WIDTH-CAR_WIDTH)//2
INITIAL_CAR_Y=SCREEN_HEIGHT-CAR_HEIGHT-50

#we initialize the game 
def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Paris Transfer demo")
    clock=pygame.time.Clock()           #work in real time

    #state variables

    car_x=INITIAL_CAR_X
    car_y=INITIAL_CAR_Y
    running=True #to keep the simulator running


    while running :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                elif event.key==pygame.K_r:
                    car_x=INITIAL_CAR_X
                    car_y=INITIAL_CAR_Y
                    print("position initialized")
        #we draw the simulation now :
        screen.fill(COLOR_BG)
        ROAD_RECT=pygame.Rect(ROAD_X,0,ROAD_WIDTH,SCREEN_HEIGHT)
        pygame.draw.rect(screen, COLOR_ROAD, ROAD_RECT)
        for y in range(0,SCREEN_HEIGHT,40):
            pygame.draw.rect(screen,COLOR_LINE,(SCREEN_WIDTH//2-2,y,4,20))
        car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        pygame.draw.rect(screen, COLOR_CAR, car_rect)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

def reset():
    return INITIAL_CAR_X,INITIAL_CAR_Y


if __name__=="__main__":
    main()