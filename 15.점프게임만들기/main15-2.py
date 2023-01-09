import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()       #파이게임을 초기화합니다.
clock = pygame.time.Clock()     #clock을 설정합니다.
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT)) #스크린을 설정합니다.

class Player():
    def __init__(self, x, y): #객체를 생성할때 초기화 한다.
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10  #객체를 생성할 때 초기화 합니다.
    
    def draw(self):             #파란색 네모를 x,y좌표에 40x40 사이즈로 그린다. 반환하는 값은 좌표와 크기이다.
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))
    
    def jump(self):         #점프 구현
        if self.isJump:
            if self.jumpCount >= -10:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= self.jumpCount**2 * 0.7 * neg
                    self.jumpCount -= 1
            else:
                    self.isJump = False
                    self.jumpCount = 10
                    
player = Player(50, MAX_HEIGHT -40) #player의 이름으로 객체를 생성. x좌표는 50 / y좌표는 바닥이다. 바닥면으로 붙이기 위해 높이에서
                                    #자신의 y크기만큼 빼준다. y좌표는 위에서 부터 0이다.
def main():
    while True :
        for evnet in pygame.event.get():
            if evnet.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if evnet.type == pygame.KEYDOWN:
                if evnet.key == pygame.K_SPACE:
                            player.isJump = True    #스페이스 키를 입력받으면 점프변수를 참으로 설정한다.
                    
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        
        player_rect = player.draw() #플레이어를 그린다. 반환하는 값은 좌표와 크기이다.
        player.jump()       #점프를 구현한다. player.isJump 변수가 참이어야 동작한다. 즉 스페이스를 누를때 동작한다.
        
        print(player_rect)
        
        pygame.display.update()
        
if __name__ == '__main__':
    main()
        
        
                        