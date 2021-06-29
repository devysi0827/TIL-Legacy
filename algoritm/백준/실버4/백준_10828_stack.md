# backjoon_10828_stack

https://www.acmicpc.net/problem/10828

# 내 풀이

```python
import sys

input = sys.stdin.readline
stack = []

command_num = int(input())

for i in range(command_num):
    command = input().split()

    if command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if stack:
            print(stack[-1])
            stack = stack[0:-1]
        else:
            print(-1)
    else:
        num = int(command[1])
        stack.append(num)
```



## 다른 방식의 풀이

- 없다

  

## 오답의 이유

-  input()으로 여러줄을 입력받을시 너무 느리다. 아래 코드를 불러와서 사용한다

  ```python
  import sys
  
  input = sys.stdin.readline
  ```



## 새롭게 알게 된 점

```python
# 인풋할 내용 = 'push 123'

 command = input().split()
```

- 이때 command는 리스트가 된다.

  - command = ['push', '123'] 

  

