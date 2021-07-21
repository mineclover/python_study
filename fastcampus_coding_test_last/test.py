def main():
    Input1 = 2000
    global Output2
    strN = str(Input1)  # 문자화
    lenN = len(strN)  # 문자길이
    len_c = (lenN // 3) * 3  # 3의 배수단위로 개수구함
    str_list = []
    i = len_c
    str_list.append(strN[0:-(len_c)])  # 처음은 따로넣음 12000의 경우 '12'부분

    while i > 3:
        str_list.append(strN[-(i):-(i - 3)])  # 3의배수 단위로 넣어줌
        i -= 3
    str_list.append(strN[-3::])  # 끝은 따로 넣음
    a = ','

    Output2 = a.join(str_list).strip(',')  # ,로 join하면서 하나로 합침
    # strip은 딱 떨어질경우 끝에 , 붙은것 제거

    print(Output2)

main()