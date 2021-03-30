def itoa(n):

    my_str = ''
    if n<0:
        n= -n
        my_str ='-'
        
        # 리스트로 나누기
    my_list = []
    while 1:
        my_list.append(n%10)
        n = n//10
        if n<10:
            my_list.append(n)
            break

        #문자화
    zero = ord("0")
    for i in range(len(my_list)-1,-1,-1):
        my_str += chr(my_list[i]+zero)

    return my_str

a = itoa(368)
b = itoa(-17)
print(type(a),a)
print(type(b),b)
