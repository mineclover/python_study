#답안
def solution(n, k): # 0
    fact = {0: 1}  # 1

    def factorial(num): # 6 : 1 가지고 옴
        if num in fact: # 7 num 안에 fact 있으면.. 1 있으면?
            return fact[num] # 8 fact[3] 가져감 아니니까 9
        val = factorial(num - 1) * num #9 3 - 1 * 3..는 3 - 1 * 3  = 6
        fact[num] = val # fact 3 = 6?
        return val # 6 리턴
#내부 변수로 선언할 수 있고


    remainder = k - 1 # 2
    seq = [i for i in range(1, n + 1)] # 1 부터 3 까지 범위의 숫자를 저장
    ans = [] # 빈 리스트
    for i in range(n - 1, 0, -1): # 4 n-1 부터 0 까지 -1 씩 이동하여 i에 채워라
        div = factorial(i) # 5 def 팩토리얼 3으로 가정함 6이 돌아옴
        val = remainder // div # 10 #
        remainder %= div # 11 div로 remainder 포하ㅗㄱ
        ans.append(seq[val]) #append로 ans에 seq[v]를 저장
        del seq[val] #
    ans.append(seq[0])
    return ans


print(solution(3, 3))
print(solution(4, 9))