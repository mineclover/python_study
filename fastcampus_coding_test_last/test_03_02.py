#함수 안에 함수 쓸 거임
#https://dojang.io/mod/page/view.php?id=2365

#N진수
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=teenager4282&logNo=220952327548

def solution(N, start, end, counts):
    answer = 0
    T = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #0~61 까지

    #단순하게 .. 그냥 해당 번호에 뭐가 있는데 그게 N 차수를 넘으면 다음 자리수로 올린다

    sl = len(start)
    data = start[sl-1] #가장 뒷자리를 가져옴


    print(T.index(start[sl-1]))

    index = T.index(data) #숫자를 sl-1 된 인덱스 값으로 줌
    #해당 인덱스 값을 받은 걸로
    #그래서 아래에서 그대로 넣음

    cur = 0  # N 초기화 해주는 친구
    for a in range(len(counts)):

        dir = index + a #시작 값 + 순서대로

        if dir == N: #현재 인덱스 ( 커서가 11이면 0으로 간다 )
            #순서가 달라서 수정함
            cur += N



            while True: # 자리 정리
                c = -2
                d = T.index(data[c])
                if d == N: #근데 두번째로 바꾼 d가 N 이라면 ( 선넘었으면 )
                    data[c] = T[0]
                    c -= 1 #다음 줄로 이동
                    if abs(c) > len(data): #c 절대값이 data 길이보다 길면
                        data.insert(0,0)
                else:
                    data[c] = T[d+1]
                    break


            T.index(data[:-1])
            print("a뭔데",T[T.index(data[1])])

            data[1] = T[T.index(data[1])]




        print(dir, N)
        print(T[dir-cur], counts[a])

        data = list(start) #리스트에 넣음
        print(data)
        data = data[:-1]
        data.append(T[dir-cur]) #전체 자리 숫자, 커서로 돌림







            #겹치는 만큼 뺌 , 카운트하고 cur x n 을 뺴도 되긴 함

        print("axxxxxx", data)

        if T[dir-cur] == counts[a]: #뒷자리 비교함
            print(T[dir-cur])
            #print("TTT",T[dir])
            print('맞다')

        else:
            print(T[dir - cur])
            #print("TTT", T[dir])
            print('틀림')


    print("ㅇㅇㅇㅇ",T[N-1]) #11이면 b 나오더라 당연하지 배열은 0부터고 숫자는 1부터 세니까



    #첫번째 자리는 N 두번째 자리는 a x N, 세번째 자리는 a x N x N 이런식임 그리고 세개를 다 합치면
    # a x N^2 + 4 뭐 이런건 이제 .. N 이 11이면 121 = 1335
    #n^3 + 4 는 1004 나오더라
    #10 x 10은 100임 a x n 이라하고 지수를 11로 잡으니까 당연히 a = N 이여서 1004 나온거임 ㅇㅋ? ㅇㅋ




    for a in range(len(start)): #2면 0,1





        pass




    return answer



#뒤로가거나 한바퀴 돌아서 꼬리 물거란 생각 안해도 됨
#(단, 2 < N <= 62, start < end이며, counts의 길이는 (end - start + 1)이다.)



def convert(n, base): #N ,
    T = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #print(T.index('0'))
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

#64 = 62 + 2 = 12 xxxxx
#ZZ = 62 + 62

#9 < Start
#Start[0] x N




#혁명이야 이건


# start , end 입력 값은 평범해보여도 N 차 함수







print(convert(63, 2))
print(convert(8, 10))
print(convert(1214, 11))

N,start,end,counts = 11,'9','d',['9', 'a', '10', '11', '12']

solution(N, start, end, counts)