PA = 100 # 초기 점수 / 플레이어 A
PB = 100 # 초기점수 / 플레이어 B
while 1: # 무한 반복 (메뉴가 3일때 브레이크는 밑에서)
    print("메뉴를 선택하시오. (1: 게임 라운드 시작, 2: 보유 점수 확인, 3: 게임 종료)")
    n = int(input()) # 메뉴 번호
    if n != 1 and n != 2 and n != 3 : # 메뉴 번후가 1~3 사이가 아니라면
        while 1:
            print("메뉴를 잘못 입력하셨습니다. 1~3 사이의 숫자를 입력하세요.\n")
            print("메뉴를 선택하시오. (1: 게임 라운드 시작, 2: 보유 점수 확인, 3: 게임 종료)")
            n = int(input()) # 1~3 사이일 때 까지 다시 받기
            if n == 1 or n ==2 or n == 3: # 1~3사이면 브레이크
                break

    if n == 1: #메뉴 번호가 1
        print("\n게임 라운드 시작을 하였습니다 \n두 사람의 주사위 숫자를 입력하세요.\n")
        a = int(input("A의 주사위 숫자 : ")) # PA
        b = int(input("B의 주사위 숫자 : ")) # PB
        print("")
        if a > 0 and a < 7 and b > 0 and b < 7: # PA와 PB가 입력한 숫자가 모두 1~6 사이라면
            if max(a, b) == a: # 승자가 PA
                PA += b * 2 # PA가 PB가 낸 숫자의 2배를 가져감
            if max(a, b) == b: # 승자가 PB
                PB += a * 2 # 위와 동일
            if min(a, b) == a: # 패자가 PA
                PA -= b # PA가 PB가 낸 숫자만큼 잃음
            if min(a, b) == b: # 패자가 PB
                PB -= a # 위와 동일

        else : # 1~6 사이가 아니면 메뉴 입력으로 돌아감
            print("\n주사위 숫자를 잘못 입력하셨습니다. 두 사람의 주사위 값을 1~6 사이의 값으로 입력하세요.")

    if n == 2: # 메뉴 번호가 2면
        print("\n보유 점수 확인을 입력하였습니다.\n")
        print("A의 보유 점수 : " , PA, ", B의 보유 점수 : ", PB, "\n") # 보유 점수 확인

    if n == 3: # 메뉴 번호가 3이면
        print("게임 종료를 입력하였습니다. 게임을 종료합니다.\n")
        print("최종 점수는 다음과 같습니다.\n")
        print("A의 최종 보유 점수 : ", PA, ", B의 최종 보유 점수 : ", PB, "\n") # 최종 보유 점수 출력
        if PA == PB : # 보유 점수가 같으면
            print("A와 B의 점수가 같습니다.") # 같다고 출력
        else: # 같지 않으면
            if PA > PB: # PA가 더 수가 크다면
                print("A가 이겼습니다.") # A가 이겼다고 출력
            if PA < PB: # PB가 더 수가 크다면
                print("B가 이겼습니다.") #B가 이겼다고 출력
        break #게임 종료




