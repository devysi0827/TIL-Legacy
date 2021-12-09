# sql 고득점 kit

1. 루시와 엘라

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM  ANIMAL_INS WHERE NAME = 'Pickle' or NAME ='Rogan' or NAME ='Sabrina' or NAME ='Mitty' or NAME ='Lucy' or NAME ='Ella' ORDER BY ANIMAL_ID
```

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM  ANIMAL_INS WHERE NAME IN('Pickle','Rogan' ,'Sabrina' ,'Mitty' ,'Lucy' ,'Ella') ORDER BY ANIMAL_ID
```



2. 이름에 EL

```mysql
SELECT ANIMAL_ID, NAME FROM  ANIMAL_INS WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE= 'Dog' ORDER BY NAME;
```



3. 중성화

```mysql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
CASE WHEN (SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%') 
THEN 'O' 
ELSE 'X' 
END 
AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
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
