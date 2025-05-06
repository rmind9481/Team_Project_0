import omok_func


def main():
    omok = omok_func.creat_omok()
    print("#######################################")
    print("###############         ###############")
    print("############### 오목게임 ##############")
    print("###############         ###############")
    print("#######################################\n\n")
    omok_func.print_omok(omok)
    print("\n\n프로그램 종료 X 입력.\n\n")

    while True:
    
        select = input("사용하실 돌을 선택해주세요. 1.'●'(흑), 2.'○'(백): ").strip()

        if select in ['x','X']:
            print("프로그램을 종료합니다.")
            break

        if select == '1':
            player = '●'
            computer = '○'
            print("플레이어는 '●'(흑), 컴퓨터는 '○'(백)입니다.")
            break
        elif select == '2':
            player = '○'
            computer = '●'
            print("플레이어는 '○'(백), 컴퓨터는 '●'(흑)입니다.")
            break
    
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

    turn = 0

    while True:
        
        if turn % 2 == 0:  # 플레이어 차례
          
            print("플레이어의 차례입니다.")
            
            x, y = omok_func.input_Check(omok)
            print(f"플레이어가가 놓은 오목의 위치 : {x},{y}")
            
 
        else:  # 컴퓨터 차례
            print("컴퓨터의 차례입니다.")
            x, y = omok_func.computer_move(omok)
            print(f"컴퓨터가 놓은 오목의 위치 : {x},{y}")

        current_player = player if turn % 2 == 0 else computer
        omok[x][y] = current_player
        omok_func.print_omok(omok)

        if omok_func.is_winner(omok, x, y, current_player):
            if current_player == player:
                print("플레이어가 승리했습니다! ")
            else:
                print("컴퓨터가 승리했습니다! ")
            break

        turn += 1





if __name__ == "__main__":
     main()