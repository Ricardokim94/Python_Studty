import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()       #파이게임을 초기화합니다.
clock = pygame.time.Clock()     #clock을 설정합니다.
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT)) #스크린을 설정합니다.

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()      #x버튼을 누르면 종료합니다.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #키다운 입력중에 스페이스가 눌리면 space를 출력합니다.
                    print("space")
            clock.tick(FPS) #FPS를 설정합니다. 1초에 몇 프레임이 동작할지 졍정합니다. 60FPS로 동작합니다.
            screen.fill((255, 255, 255)) #화면을 흰색으로 채웁니다.
            
            pygame.display.update()
if __name__ == '__main__':
    main()