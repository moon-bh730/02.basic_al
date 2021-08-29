## 오류 수정 1
## 블럭 회전이 잘 작동하도록 처리

import sys
import time as tm
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, \
    K_LEFT, K_RIGHT, K_DOWN, K_SPACE

BLOCK_DATA = (
    (
        (0, 0, 1, \
         1, 1, 1, \
         0, 0, 0),
        (0, 1, 0, \
         0, 1, 0, \
         0, 1, 1),
        (0, 0, 0, \
         1, 1, 1, \
         1, 0, 0),
        (1, 1, 0, \
         0, 1, 0, \
         0, 1, 0),
    ), (
        (2, 0, 0, \
         2, 2, 2, \
         0, 0, 0),
        (0, 2, 2, \
         0, 2, 0, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 2, \
         0, 0, 2),
        (0, 2, 0, \
         0, 2, 0, \
         2, 2, 0)
    ), (
        (0, 3, 0, \
         3, 3, 3, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 3, 0),
        (0, 0, 0, \
         3, 3, 3, \
         0, 3, 0),
        (0, 3, 0, \
         3, 3, 0, \
         0, 3, 0)
    ), (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ), (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ), (
        (0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0)
    )
)

##------------------------------------------
## 함수 선언부 -----------------------------
##------------------------------------------
class Block:
    def __init__(self, count):
        self.turn = randint(0, 3)                   # 블록의 방향(0~3)
        self.type = BLOCK_DATA[randint(0, 6)]       # 블록타입(6가지)
        self.data = self.type[self.turn]            # 블록데이터(현재 방향)
        self.size = int(sqrt(len(self.data)))       # 블록 크기
        self.xpos = randint(2, 8-self.size)         # 블록 랜덤좌표 x
        self.ypos = 1 - self.size                   # 블록 랜덤좌표 y
        self.fire = count + INTERVAL                # 낙하 시작시간
    
    def update(self, count):            #블록의 낙하, 이동을 처리한다.
        erased = 0
        # x_offset, y_offset 현재 화면의 포커스 위치값
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):     # ypos + 1 상태가 겹치는지 확인
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    if 0 <= self.xpos+x_offset < WIDTH and \
                        0 <= self.ypos+y_offset < HEIGHT:
                        val = BLOCK.data[y_offset*BLOCK.size \
                                        + x_offset]
                        if val != 0:
                            FIELD[self.ypos+y_offset]\
                                [self.xpos+x_offset] = val
            
        erased = erase_line()                       
        go_next_block(count)
        
        if self.fire < count:                   # 현재 낙하중이면   
            self.fire = count + INTERVAL        # 다음 낙하 시간설정
            self.ypos += 1                      # 1단계 낙하 이동
        return erased

    def draw(self):
        for index in range(len(self.data)):
            xpos = index % self.size
            ypos = index // self.size
            val = self.data[index]
            if 0 <= ypos + self.ypos < HEIGHT and \
                0 <= xpos + self.xpos < WIDTH and val != 0:
                x_pos = 25 + (xpos + self.xpos) * 25
                y_pos = 25 + (ypos + self.ypos) * 25
                pygame.draw.rect(SURFACE, COLORS[val], 
                                    (x_pos, y_pos, 24, 24))

def erase_line():                       # 행이 모두 찬 단을 지우는 작업
    erased = 0
    ypos = 20
    while ypos >= 0:
        if all(FIELD[ypos]):            # 싸여진 블록중 모두 찬 블록 이라면?
            erased += 1
            del FIELD[ypos]
            FIELD.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
        else:
            ypos = -1
    return erased

def is_game_over():
    filled = 0
    for cell in FIELD[0]:
        if cell != 0:
            filled += 1
    return filled > 2               # 2 = 좌우의 벽

def go_next_block(count):               #다음 블록으로 전환한다.
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)

# xpos, ypos 좌표에서 turn방향 블록이 벽, 바닥 또는 싸여있는 블록과 충돌 하는지 반환하는 함수
def is_overlapped(xpos, ypos, turn):    
    data = BLOCK.type[turn]             # 현재 블록의 방향 확인
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size):
            if 0 <= xpos+x_offset < WIDTH and \
                0 <= ypos+y_offset < HEIGHT:
                # 블럭에 숫자가 있고 and 그자리에 숫자가 있으면
                if data[y_offset*BLOCK.size + x_offset] != 0 and \
                    FIELD[ypos+y_offset][xpos+x_offset] != 0:       
                    return True
    return False

##------------------------------------------
## 전역 변수부 -----------------------------
##------------------------------------------
pygame.init()
pygame.key.set_repeat(30, 30)
SURFACE = pygame.display.set_mode([600, 600])
FPSCLOCK = pygame.time.Clock()
WIDTH = 12                                          # 게임판(FIELD)의 너비
HEIGHT = 22                                         # 게임판(FIELD)의 높이
INTERVAL = 40                                       # 게임 낙하 시간 간격(게임 속도-시간이 갈수록 빨라짐)
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]   #블록이 쌓여진 정보값
COLORS = ((0, 0, 0), (255, 165, 0), (0, 0, 255), (0, 255, 255), \
            (0, 255, 0), (255, 0, 255), (255, 255, 0), (255, 0, 0), (128, 128, 128))        # 색배열 튜플
BLOCK = None                                        # 현재 낙하중인 블록객체
NEXT_BLOCK = None                                   # 다음에 낙하할 블록객체

                        # BLOCK을 한칸씩 낙하
                        # FIELD 낙하 불가할(낙하 완료) 경우 BLOCK의 내용을 FIELD에 복사한다.

##------------------------------------------
## 메인 코드부 -----------------------------
##------------------------------------------
def main():
    global INTERVAL
    count = 0           # 시간관리 카운트
    score = 0           # 점수
    game_over = False                               # 게임오버 여부 플래그
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)       # GAME OVER!! 표시
    message_over = largefont.render("GAME OVER!!", True, (0, 255, 255))
    message_rect = message_over.get_rect()
    message_rect.center = (300, 300)                # 메시지 초기화

    go_next_block(INTERVAL)                         # 다음에 낙하할 블록 초기화

    for ypos in range(HEIGHT):
        for xpos in range(WIDTH):                   # 2차원 배열 초기화
            FIELD[ypos][xpos] = 8 if xpos == 0 or \
                xpos == WIDTH -1 else 0             # 좌우벽을 8로 채우고, 공백은 0으로 채우기
    for index in range(WIDTH):
        FIELD[HEIGHT-1][index] = 8                  # 바닥벽을 8로 채움

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
        
        game_over = is_game_over()                  # 게임 오버인지 판정
        if not game_over:
            count += 5                              # 레벨 업을 위한 카운트 5씩 증가
            if count % 1000 == 0:
                INTERVAL = max(1, INTERVAL -2)      # 하강 속도를 증가(1보다 작지 않게)
            erased = BLOCK.update(count)            # update로 블록 이동시키고, 파괴하여 삭제한 행수 반환

            if erased > 0:                          # 파괴한 블럭의 배수만큼 점수 누적
                score += (2 ** erased) * 100

            # 키 이벤트 처리
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn      # 현재 스크린 좌표값 대입
            # 입력한 키값을 좌표에 반영
            if key == K_SPACE:
                next_t = (next_t + 1) % 4
            elif key == K_RIGHT:
                next_x += 1
            elif key == K_LEFT:
                next_x -= 1
            elif key == K_DOWN:
                next_y += 1

            # 벽, 바닥 또는 싸여있는 블록과 충돌 하는지 확인
            if not is_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x                     #키에따른 위치 조정
                BLOCK.ypos = next_y                     #키에따른 위치 조정
                BLOCK.turn = next_t                     #키에따른 방향전환
                BLOCK.data = BLOCK.type[BLOCK.turn]     # ???

            # 전체 & 낙하중인 블록 그리기
            SURFACE.fill((0, 0, 0))                     #검은색으로 채우기
            for ypos in range(HEIGHT):
                for xpos in range(WIDTH):
                    val = FIELD[ypos][xpos]
                    pygame.draw.rect(SURFACE, COLORS[val], 
                                    (xpos*25 + 25, ypos*25 + 25, 24, 24))       # FIELD그리기
            BLOCK.draw()                                #떨어지는 블록 그리기

            # 다음 나올 블록 그리기
            for ypos in range(NEXT_BLOCK.size):
                for xpos in range(NEXT_BLOCK.size):
                    val = NEXT_BLOCK.data[xpos + ypos*NEXT_BLOCK.size]
                    pygame.draw.rect(SURFACE, COLORS[val],
                            (xpos*25 + 460, ypos*25 + 100, 24, 24))

            # 점수 표시
            score_str = str(score).zfill(6)
            score_image = smallfont.render(score_str, True, (0, 255, 0))
            SURFACE.blit(score_image,(500, 30))     

            if game_over:
                SURFACE.blit(message_over, message_rect)

            pygame.display.update()
            FPSCLOCK.tick(15)

# 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드를 돌리라
if __name__ == "__main__":
    main()