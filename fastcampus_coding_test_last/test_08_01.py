#N 보드의 크기, K 사과의 갯수, 뱀의 방향 변환 함수? # 뱀의 방향 정보 권한?
#인자전달과 레퍼런스 전달
#https://andamiro25.tistory.com/33

#1, 앞자리를 추가하고 뒷자리를 날린다
#2, 가장 앞에 있는 것부터 하나씩 이동한다.
#뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

def solution(N, K, L, apples, moves):

    #N = 행
    #K = 사과 갯수
    #L = 방향
    #사과 위치
    #뱀 이동
    body = 1 #뱀 몸 갯수 머리 포함
    head = [[1,1]]
    dic = 0 # 방향 지시 숫자
    LL = [[0,1],[-1,0],[0,-1],[1,0]] #방향 데이터
    #왼쪽은 + , 오른쪽은 -로 인덱스 접근
    #a = [(x+1,y+1) for x in range(N) for y in range(K)] #오 그냥 생각하는대로 했는데 됨
    aa = [(x+1,y+1) for x in range(N) for y in range(N)] #오 그냥 생각하는대로 했는데 됨

    print(aa)

    x = 0
    # apples = [(3, 4), (2, 5), (5, 3)]
    # moves = [(3, 'D'), (15, 'L'), (17, 'D')]
    clean = []
    while True:
        #head.insert(0,head[0])


        if x == 0: #시간 0일 땐 그냥 추가
            head.append(head[0])
            pass
            #주소 참조가 계속 말썽인데 어케 해결함?

        else: #아닐 때도 추가하고 값 바꿈 #꼬리
            head.insert(0, head[0])

            print("값 추가함") #머리이동
            i = head[0][0] + int(LL[dic][0])
            j = head[0][1] + int(LL[dic][1])
            head[0] = [i,j] #이렇게 해야 안겹치게 나오는 거 같네

        print("헤드",head)
        print(apples)
        #print("사과찾",tuple(head[0]) in apples,tuple(head[0]))
        if tuple(head[0]) in apples: #해드 주소에 애플이 있으면 == True 하면 안됨 뭐야 이거 ;
            print("사과다")
            for a in clean: #먹었던 건지 새로운 건지 검증
                if a == head[0]: #먹었음
                    del head[body]
                    break
            else:
                clean.append(head[0])
                print("사과 먹음 , 없어서 추가함")

           #중복되도 상관 없잖아?
            print("클린",clean,"헤드",head)
            print("뭐라 뜨길래",clean.index(head[0]))

        else:  # 길 지나감
            del head[body]



        tit = []
        for a in range(len(moves)):
            tit.append(moves[a][0])
        #무브 시간만 가져옴
        print("이동할 시간 : ",x in tit)
        #tit 안에 무브시간 있는지 확인
        if x in tit:
            for a in range(len(moves)):
                if moves[a][0] == x: #숫자 맞는지 검증
                    if moves[a][1] == 'D': #오른쪽
                        print("D")
                        dic -= 1
                        if dic == -1:
                            dic = 3

                    elif moves[a][1] == 'L':
                        print("L")
                        dic += 1
                        if dic == 4:
                            dic = 0


                    else:
                        print("못찾음")


        print("최종 현재 뱀 길이 : ",head)
        print(tuple(head[0]) not in aa)
        if head[0] in head[1:] == True:
            return x
        if (tuple(head[0]) not in aa) == True:
            return x
        x += 1



N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves))

N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))

N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))