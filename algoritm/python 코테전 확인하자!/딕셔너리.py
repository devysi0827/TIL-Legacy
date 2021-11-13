# 1. 정의
dict_sample = {}
print('#1')
print(dict_sample)
# 2. 추가하기
print('#2')
dict_sample['first'] = 'firstadd'
print(dict_sample)
print(dict_sample['first'])
# 3. 수정하기
print('#3')
dict_sample['first'] = 'firstresume'
print(dict_sample)
print(dict_sample['first'])
# 4. 삭제하기
print('#4')
del dict_sample['first']
print(dict_sample)
#5. key, value, items를 각각 얻기
print('#5')
dict_sample['first'] = '1'
dict_sample['second'] = '2'
dict_sample['third'] = '3'
print(dict_sample)
print(list(dict_sample.keys()))
print(list(dict_sample.values()))
print(list(dict_sample.items()))
#6. 안에 있는 지 확인하기
print('#6')
print('four' in dict_sample)
print('third' in dict_sample)