def solution(N, start, end, counts):
    answer = 0
    return answer


#검증페이지고 .. 그냥 남겨두기로 함



#뒤로가거나 한바퀴 돌아서 꼬리 물거란 생각 안해도 됨
#(단, 2 < N <= 62, start < end이며, counts의 길이는 (end - start + 1)이다.)

#알파벳은 26자

#소문자는 97부터 대문자는 65부터 시작하고 , 소문자 z에서 대문자 A 로 가는 것에는 -79 가 필요함
#아스키코드의 숫자는 48이 0으로 57이 9 총 10개임
#숫자 9에서 소문자 a로 가려면 + 65를 해줘야함

#


print(ord('a'))
print(ord('b'))
print(ord('A'))

for a in range(122):
    b = chr(a)
    print("숫자 ",a,"변환 : ", chr(a), b+b, type(b))

    try:
        b = int(b)
        print(b+b)
    except Exception:
        pass

#검증함 chr으로 변환한게 저장되는지, 변환되는지 , 잘됨


N,start,end,counts = 14,9,'d',['9', 'a', 'c', 'd', 'e']

solution(N, start, end, counts)