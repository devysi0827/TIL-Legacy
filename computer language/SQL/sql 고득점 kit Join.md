# sql 고득점 kit

![image-20211204060512355](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20211204060512355.png)

https://pearlluck.tistory.com/46

1. 없어진 기록 찾기

```mysql
SELECT
    outs.animal_id, outs.name
FROM animal_outs AS outs
	LEFT JOIN animal_ins AS ins
	ON outs.animal_id = ins.animal_id
WHERE
    ins.animal_id IS NULL;
```



2. 있었는데요 없었습니다.

```mysql
-- 코드를 입력하세요
SELECT
    ins.animal_id, ins.name
FROM animal_ins AS ins
	LEFT JOIN animal_outs AS outs
	ON outs.animal_id = ins.animal_id
    where outs.DATETIME < ins.DATETIME
ORDER BY
    ins.DATETIME 
```



3. 오랜기간 보호한 동물(1)

```mysql
-- 코드를 입력하세요
SELECT
    ins.NAME, ins.DATETIME
FROM animal_ins AS ins
	LEFT JOIN animal_outs AS outs
	ON outs.animal_id = ins.animal_id
    where outs.DATETIME IS NULL
ORDER BY
    ins.DATETIME ASC
LIMIT 3;
```



4. 오랜기간 보호한 동물

```mysql

```



5. DATETIME에서 DATE로 형변환

```mysql
-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME,DATE_FORMAT(DATETIME,'%Y-%m-%d') AS 날짜 FROM ANIMAL_INS ORDER BY ANIMAL_ID
```



in

%

case when then else end

date_format(column,'')
