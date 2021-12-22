# 비동기 vs 동기

### 개념

- 동기: 동기식 처리 모델(Synchronous processing model)은 직렬적으로 태스크(task)를 수행한다.

  즉, 태스크는 순차적으로 실행되며 어떤 작업이 수행 중이면 다음 작업은 대기하게 된다.

- 비동기: 비동기식 처리 모델(Asynchronous processing model 또는 Non-Blocking processing model)은 병렬적으로 태스크를 수행한다.

  즉, 태스크가 종료되지 않은 상태라 하더라도 대기하지 않고 다음 태스크를 실행한다.

![img](https://blog.kakaocdn.net/dn/cuo0zV/btqF1nvdCLR/FxeSRt6m79u781P0Nfey9k/img.png)



### javascript is single threads

- 자바는 단일스레드이기 때문에 한 번의 한 작업밖에 할 수 없다.
- worker thread를 따로 만들어서 이와 같은 문제(blocking: 시간지연)를 해결한다.

```
  Main thread: Task A --> Task C
Worker thread: Expensive task B
```



### 비동기 문제와 promise

- 특정 결과가 없다면 오류가 나는 코드가 있을 때, promise를 이용하여 비동기를 동기화 할 수 있습니다.
- 이 작업은 메인스레드를 차단하지 않으므로, 메인스레드는 계속 진행됩니다.