# sql 고득점 kit

1. GROUP BY

```mysql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```



2. 동명 동물 수 찾기

```mysql
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >1 ORDER BY NAME;
```



3. 입양시간 구하기

```mysql
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS DATETIME FROM ANIMAL_OUTS WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <20 GROUP BY HOUR ORDER BY HOUR ;
```



4. 입양시간 구하기2 (VERY HARD)

```mysql
-- 코드를 입력하세요
SET @HOUR = -1;
SELECT (@HOUR:= @HOUR +1) AS HOUR,
(SELECT COUNT(HOUR(DATETIME)) 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME)=@HOUR) AS COUNT 
FROM ANIMAL_OUTS
WHERE @HOUR <23;
```



SET, @HOUR, AS, GROUP BY, HAVING
