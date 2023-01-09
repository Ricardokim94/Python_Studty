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
                    
class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self) :
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 40))
    
    def move(self, speed):
        self.x = self.x - speed #화면의 오른쪽 끝에서 왼쪽으로 이동하는 함수입니다.
        if self.x <= 0:
            self.x = MAX_WIDTH

player = Player(50, MAX_HEIGHT - 40)
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40)

def main():
    
    speed = 7   #적의 스피드 = 7
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                            player.isJump = True
            
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        
        player_rect = player.draw()
        player.jump()
        
        enemy_rect = enemy.draw()   #적을 그립니다.
        enemy.move(speed)   #속도가 0.01씩 빨라집니다.
        speed = speed + 0.01
        
        if player_rect.collidedict(enemy_rect): #플레이어와 적과 충돌하면 종료합니다.
            print("충돌!!!!")
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
    
if __name__ == '__main__':
    main()
    
    