def solution(new_id):

    id_1 = new_id.lower()  #1 더 할 필요없음

    special_word = '+~!@#$%^&*()=[{]}:?,<>/'  #2 더 할 필요없음
    special_word = list(special_word)
    id_2 = []
    id_1 = list(id_1)
    for ele in id_1:
        if ele not in special_word:
            id_2.append(ele)

    id_3 = list(id_2)  #3 더 할 필요없음
    count = 0
    for i in range(len(id_2)-1):
        if id_2[i] =='.' and id_2[i] == id_2[i+1]:
            del id_3[i-count]
            count +=1

    if len(id_3) != 0:  #4 더 해야함
        if id_3[0] == '.':
            del id_3[0]
        if len(id_3) != 0:
            if id_3[-1] == '.':
                del id_3[-1]

    if len(id_3) ==0:  #5 여기서 빈문자라면
        id_3.append('a')

    id_3 =id_3[0:15]  #6 더 할 필요없음

    if len(id_3) != 0:  #4 더 해야함
        if id_3[0] == '.':
            del id_3[0]
        if len(id_3) != 0:
            if id_3[-1] == '.':
                del id_3[-1]

    while len(id_3) < 3:  #7
        id_3 += id_3[-1]
    answer = ''.join(id_3)
    return answer

new_id = "=.="
solution(new_id)


# del_list = []
    # for i in range(len(id_3)):
    #     if id_3[i] == ' ' :
    #         del_list.append(i)
    #
    # if del_list:
    #     for i in range(len(del_list)-1,-1,-1):
    #         del id_3[del_list[i]]