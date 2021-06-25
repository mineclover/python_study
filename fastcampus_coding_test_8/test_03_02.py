#함수 안에 함수 쓸 거임
#https://dojang.io/mod/page/view.php?id=2365

#N진수
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=teenager4282&logNo=220952327548

def solution(N, start, end, counts):
    answer = 0
    T = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #0~61 까지

    #단순하게 .. 그냥 해당 번호에 뭐가 있는데 그게 N 차수를 넘으면 다음 자리수로 올린다

    data = list(str(start))  # 리스트에 넣음

    #해당 인덱스 값을 받은 걸로
    #그래서 아래에서 그대로 넣음
    cur = 0  # N 초기화 해주는 친구

    for f in range(len(counts)): # count갯수만큼
        if f == 0:
            index = T.index(data[-1])  # 시작값을 가져옴, 첫째 자리 숫자 확인
        print("인덱스",index)
        dir = index + f #시작 값 + 순서대로
        # count와 스타트 엔드간의 1대 1 비교로 정답확인 하기
        #
        if dir -cur >= N: #현재 인덱스 ( 만약 커서가 11이면 0으로 간다 )
            #자리 값 바뀔 때 여길 들어오면 안되는데 지금 들어오고 있음

            cur += dir # 0부터 시작할 수 있게 dir에 dir를 빼게 함
            #커서가 한번 반복 됬으므로
            c = -2 #두번째 자리
            while True: # 자리 정리
                try:
                    d = T.index(data[c]) #두번째 자리수의 문자 값을 봄
                except IndexError:
                    data.insert(0,T[1]) #값이 없으면 오류남 그래서 추가해줌, #0는 0이기 때문에 1부터 시작함
                    d = T.index(str(data[c])) #그리고 추가한 후에 값을 다시 봄


                if d+1 >= N: #근데 두번째로 바꾼 d가 N 이라면 ( 선넘었으면 )
                    data[c] = T[0]
                    print("자리수이동")
                    c -= 1 #다음 줄로 이동
                else:

                    d = T.index(data[c])
                    print("인데에", data[c])
                    data[c] = T[d]
                    print(d+1)
                    print("추가함",data)

                    break


        print("53번째 줄",dir, N)
        print(T[dir], counts[f])


        print(data)
        data = data[:-1]

        data.append(T[dir-cur]) #전체 자리 숫자, dir로 돌림
        print("추가된 글씨",T[dir-cur], dir,cur)


            #겹치는 만큼 뺌 dir 카운트 유지 , 카운트하고 cur x n 을 뺴도 되긴 함

        print("axxxxxx", data)
        ''.join(data)
        if ''.join(data) == counts[f]: #뒷자리 비교함
            print(''.join(data))
            #print("TTT",T[dir])
            print(''.join(data) , counts[f] ,'맞다')

        else:
            print(T[dir - cur])
            #print("TTT", T[dir])
            print(''.join(data) , counts[f] ,'틀림')


    print("ㅇㅇㅇㅇ",T[N-1]) #11이면 b 나오더라 당연하지 배열은 0부터고 숫자는 1부터 세니까



    #첫번째 자리는 N 두번째 자리는 a x N, 세번째 자리는 a x N x N 이런식임 그리고 세개를 다 합치면
    # a x N^2 + 4 뭐 이런건 이제 .. N 이 11이면 121 = 1335
    #n^3 + 4 는 1004 나오더라
    #10 x 10은 100임 a x n 이라하고 지수를 11로 잡으니까 당연히 a = N 이여서 1004 나온거임 ㅇㅋ? ㅇㅋ






    return answer



#뒤로가거나 한바퀴 돌아서 꼬리 물거란 생각 안해도 됨
#(단, 2 < N <= 62, start < end이며, counts의 길이는 (end - start + 1)이다.)


N, start, end, counts = 62, 'v', 'y', ['v', 'w', 'x', 'y']

print(solution(N, start, end, counts))








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

# print(convert(63, 2))
# print(convert(8, 10))
# print(convert(1214, 11))


