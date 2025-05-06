import random
# 컴퓨터가 랜덤하게 숫자 지정시 필요


# 1. 오목 판을 리스트에 담는다.
# 2. 2차원 리스트 이용해서 좌표 설정

def creat_omok():
    omok_borad = []

    for i in range(12):
        omok_dot = ["."]*12
        omok_borad.append(omok_dot)
    return omok_borad

# 오목판 화면 출력
# 3. 좌표를 화면에 . 으로만 표시

def print_omok(omok_board):
    
    for i in omok_board:
        print("  ".join(i))
    print()

# 4. 유저에게 좌표 입력받기

# ------------------------------------------------------------------------------
# 함수 기능 :
# 4. 유저가 입력한 좌표 값이 올바른지 판별하기 
# =>4-1. 숫자 그리고 , 를 입력했는지,특수문자 숫자 외의 번호가 나왔을때 체크하고
# =>4-2. 바둑판 좌표를 벗어난 숫자인지 체크
# =>4-3. 해당 좌표에 돌이 없는지 체크
# =>4-4. 올바르게 입력할때 까지 반복
# =>4-5. 바르게 된 입력값 반환
 
# 반환 값   : 2가지 정수 출력
# try:
# expext 예외 처리 => ValueError
# -----------------------------------------------------------------------------

# 플레이어가 얼마나 입력할지 모른다. 그래서 무한반복

def input_Check (omok_board):
    while True:
        
        try:
            
            x, y = map(int, input("오목 좌표 (X, Y)를 입력해주세요. : ").strip().split(','))

        # 범위 체크
            if not (0 <= x < 11 and 0 <= y < 11):
                print(f"{x},{y} 범위를 초과했습니다. (범위: 0 ~ 14) 다시 입력해 주세요.")
                continue
        # 돌 있는지 체크
            elif omok_board[x][y] != ".":
                print(f"{x},{y} 자리에 이미 돌이 있습니다. 다시 입력해 주세요.")
                continue           
            return  x, y
    
        except ValueError:
                print("잘못된 입력 값입니다.")
                continue


# 승리 조건 매서드 2차원 보드판을 불러온다.
# 현재 플레이어가 둔 위치점에서 플레이어 랑 같은것을 판별
#
#       ↖ ↑ ↗  
#       ← ● → 
#       ↙ ↓ ↘
#


def is_winner(omok_board, x, y, player):
    directions = [
        (1, 0),  # 수평
        (0, 1),  # 수직
        (1, 1),  # 대각선 (\)
        (1, -1), # 대각선 (/)
    ]
    
    # 현재 x,y 지점에서 for 반복문을 써서 한칸씩 증가하여 위치를 찾는다.
    for dx, dy in directions:
        count = 1
        # 1에서 5까지 반복해서 앞쪽(양수) 방향을 확인한다 1에서 5까지 반복해서  
        for i in range(1, 5): 
            nx, ny = (x + dx * i), (y + dy * i)
            if 0 <= nx < 11 and 0 <= ny < 11 and omok_board[nx][ny] == player:
                count += 1
            else:
                break

        # 1에서 5까지 반복해서 뒷쪽(음수) 방향을 확인한다 5칸 
        for i in range(1, 5):
            nx, ny =(x - dx * i), (y - dy * i)
            if 0 <= nx < 11 and 0 <= ny < 11 and omok_board[nx][ny] == player:
                count += 1
            else:
                break
        # 같은 돌의 개수가 5개 이상이라면 승리
        if count >= 5:
            return True
        
    #그렇지 않다면 False 값을 리턴한다.
    return False


# 컴퓨터가 (0~11)
def computer_move(board):

    while True:
        x, y = random.randint(0, 11), random.randint(0, 11)

   
        if board[x][y] == ".":
            return x, y
        



