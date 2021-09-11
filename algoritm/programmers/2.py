import math

def solution(fees, records):
    # records 만들기
    car_record = []
    for i in range(len(records)):
        temp = records[i].split(" ")
        car_record.append(temp)

    # 차량 번호 정리
    car_id = []
    for i in range(len(car_record)):
        if car_record[i][1] not in car_id:
            car_id.append(car_record[i][1])
    car_id = sorted(car_id)

    # car 딕셔너리
    car_dict = {}
    for i in range(len(car_id)):
        car_dict[car_id[i]] = 0

    for i in range(len(car_id)):
        time = 23 * 60 + 59
        du_time = 0
        for j in range(len(car_record)):
            if car_id[i] == car_record[j][1]:
                if car_record[j][2] == "IN":
                    temp_time = car_record[j][0].split(":")
                    time = int(temp_time[0]) * 60 + int(temp_time[1])
                if car_record[j][2] == "OUT":
                    temp_time = car_record[j][0].split(":")
                    out_time = int(temp_time[0]) * 60 + int(temp_time[1])
                    du_time += (out_time - time)
                    time = 23 * 60 + 59
        du_time += 23 * 60 + 59 - time
        if du_time <= fees[0]:
            car_dict[car_id[i]] += fees[1]
        if du_time > fees[0]:
            car_dict[car_id[i]] += fees[1] + math.ceil((du_time - fees[0]) / fees[2]) * fees[3]

    sorted_car_dict = sorted(car_dict.items(), key=lambda item: item[0])

    # 정답 양식 맞추기
    answer = []
    for total_fee in sorted_car_dict:
        answer.append(total_fee[1])

    return answer

    # return sorted_car_dict