#함수 안에 함수 쓸 거임
#https://dojang.io/mod/page/view.php?id=2365

#N진수
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=teenager4282&logNo=220952327548

def solution(N, start, end, counts):
    answer = 0
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



#print(T.index('0'))
#whssk gurauddldi dlrjs







print(convert(63, 2))
print(convert(233, 2))
print(convert(233, 16))

N,start,end,counts = 14,9,'d',['9', 'a', 'c', 'd', 'e']

solution(N, start, end, counts)