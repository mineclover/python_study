## 과제2.
#인스턴스변수
#https://wikidocs.net/1744
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=beaqon&logNo=221045631119
#인스턴스 변수가 꼭 class 이름(오브젝트) 에 (오브젝트를 달고 있지 않아도 됨)
'''
----
철수는 개발자에서 은퇴하여 치킨집을 하게 되었다.
철수는 뛰어난 개발 실력으로 를N대의 자동 튀김기 만들어냈다.
i번째 자동 튀김기는 치킨을 한 번 튀기는 데에 fry[i] 만큼의 시간이 걸리며,
튀김이 한번 끝나면 clean[i] 만큼의 시간동안 자동 세척을 한다.

철수가 C 번 치킨을 튀겨내려고 할 때, 최소한 몇 시간 동안 자동 튀김기를 가동해야 하는지 계산하시오.

제약 사항
- 0 < N <= 100000
- fry[i]는 0 < fry[i] <= 100를 만족하는 정수
- clean[i]는 0 < clean[i] <= 100를 만족하는 정수
- 0 < C <= 100000


- 입출력 예


  | N | fry | clean | C | return |
  |---|-----|-------|---|--------|
  | 2 | `[3, 6]` | `[2, 1]` | 20 | 58 |
  | 4 | `[2, 2, 1, 3]` | `[2, 4, 3, 2]` | 2 | 2 |
'''

#방법 1번 ,
# 변수 안에 클래스를 선언하고, 클래스 안에 현재 뭐 하고 있는지 확인하는 것을 넣어
# 모든 게 작동하는 작동 변수를 넣고 , 치킨이 들어감 변수를 기준으로 작동 시킴
# 시간 업데이트 변수를 넣어 > 공통 사용 변수로 처리함 > 공통적으로 사용하는 변수가 시간인데
# 그 시간에 대응했을 때 0 이 되는 애들이 있으면,
# 요리 끝, 처리 클린 처리로 들어감
# 튀김 시작 시간, 끝 시간을 넣고, 클리닝 시작시간 끝시간을 넣는 것
# 요리는 튀김을 기준으로 하기 때문에 , 여러개 해서 가동되야하지 않는 이상 튀김 끝 하면 튀김 갯수 올라가는 것임 튀김 갯수 맞으면 바로 작동 종료

#인스턴스변수 생성자 소멸자 https://blog.hexabrain.net/285
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=beaqon&logNo=221045631119

#크기 순서대로 번호 매기기
#https://gomming.tistory.com/28

class Frying_machine:
    fry_chicken = 0
    #이렇게 밖에 빼놔야 외부에서 Frying_machine.fry_chicken 으로 가져와짐

    def __init__(self,fry,cleen):
        self.fry = fry
        #None -> f -> 0
        self.cleen = cleen
        self.frying = False
        self.cooking_time = 0
        #frying 이 활성화되면 시간이 올라감
        #쿠킹 타임이 = fry 일 때 요리가 나오고
        #쿠킹 타임이 = fry+cleen 일 때 fry와 cooking_time 이 0이 됨
        #a 는 고유번호, 제자리 찾아가는 용도 쿠킹 타임이 끝나면 , 고유 번호가 레벨을 가지고 베열로 돌아감



def solution(N, fry, clean, C):
    answer = 0
    b = [0 for a in range(N)]

    Queuing = fry # 찾을 수 있어야하니까




    for a in range(N): # 기계 배치하기

        print(Queuing)
        b[a] = Frying_machine(fry[a], clean[a])
        print(a,":",b[a].fry, b[a].cleen,b[a].frying,b[a].cooking_time)



    while True:

        #잠만 근데 최초 사용 때는 닦는게 느려도 빨리 구워지는 걸로 넣는게 좋은데?
        #사용 중 안풀리면 원래 값 이니까
        #

        if Frying_machine.fry_chicken == N:
            return answer

        #오븐 사용 중인 거 체크
        for a in range(N): #사용 중(frying)이면 1000, 아니면 원래 값
            if b[a].frying == True:
                Queuing[a] = 1000
            else:
                b[a].level = b[a].fry

        #확인한 오븐 중 가장 빠른 것에 고기 넣음
        if min(Queuing) != 1000: #현재 대기열 최소값이 가장 작은게 1000이 아니면
            b[Queuing.index(min(Queuing))].frying = True

        #넣은 고기가 잘 구워지고 있나 확인

        for a in range(N):
            #다 구움
            if b[a].cooking_time == b[a].fry:
                Frying_machine.fry_chicken += 1
            #다 닦음
            if b[a].cooking_time == b[a].fry + b[a].cleen:
                b[a].frying = False
                b[a].cooking_time = 0

            #오븐 쓰고 있음 (굽고 있음, 닦고 있음
            if b[a].self.frying == True:
                b[a].cooking_time += 1

        answer += 1
        print(answer)






    for a in range(N):
        b[a].fry

    print("가장 작은 수", min(Level))  # 가장 작은 수 찾기
    print(Level.index(min(Level)))  # 가장 작은 수의 인덱스 찾기


    print("가장 작은 수", min(Level))  # 가장 작은 수 찾기
    print(Level.index(min(Level)))  # 가장 작은 수의 인덱스 찾기



N, fry, clean, C = 4,[2, 2, 1, 3],[2, 4, 3, 2],2

print(solution(N, fry, clean, C))