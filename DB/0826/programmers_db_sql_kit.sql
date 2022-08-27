-- 프로그래머스 sql 고득점 kit

1) select
--1 모든 레코드 조회하기
SELECT*from ANIMAL_INS order by ANIMAL_ID

--2 역순 정렬하기
SELECT NAME,DATETIME from ANIMAL_INS order by ANIMAL_ID DESC

--3 아픈 동물 찾기
SELECT ANIMAL_ID, NAME from ANIMAL_INS WHERE INTAKE_CONDITION = 'sick'

--4 어린 동물 찾기
SELECT ANIMAL_ID, NAME from ANIMAL_INS
where INTAKE_CONDITION != 'Aged'
order by ANIMAL_ID;

--5 동물의 아이디와 이름
SELECT ANIMAL_ID,NAME from ANIMAL_INS
order by ANIMAL_ID

--6 여러 기준으로 정렬하기
SELECT ANIMAL_ID,NAME,DATETIME  from ANIMAL_INS
order by NAME, datetime desc

--7 상위 n개 레코드
SELECT name from ANIMAL_INS
order by datetime limit 1

2) sum , max , min
--1 최댓값 구하기 (max 이용해도 됨)
SELECT datetime as "시간" from animal_ins
order by datetime desc limit 1

--2 최솟값 구하기 (min 이용해도 됨)
SELECT datetime as 시간 from animal_ins
order by datetime limit 1

--3 동물 수 구하기
SELECT count(*) from animal_ins

--4 중복 제거하기
SELECT COUNT(DISTINCT NAME) AS 'count'
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

3) GROUP BY
--1 고양이와 개는 몇 마리 있을까 ?
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as 'count'
from animal_ins
group by ANIMAL_TYPE
order by ANIMAL_TYPE

--2 동명 동물 수 찾기
SELECT name, count(name) as "COUNT" from ANIMAL_INS
group by name
having count(name) >= 2
order by name

--3 입양 시각 구하기(1)
SELECT HOUR(datetime) AS "HOUR" , count(HOUR(datetime)) as "COUNT"
from ANIMAL_OUTS
where HOUR(datetime) >= 9  AND HOUR(datetime) < 20
group by HOUR(datetime)
order by HOUR(datetime)

--4 입양 시각 구하기(2)
set @hour = -1;
SELECT (@hour := @hour +1) AS "HOUR", 
(select count(datetime) from ANIMAL_OUTS
 where hour(datetime) = @HOUR) AS "COUNT"
from ANIMAL_OUTS
where @HOUR < 23

4) IS NULL
--1 이름 없는 동물의 아이디
SELECT ANIMAL_ID from ANIMAL_INS
where name is null

--2 이름 있는 동물 아이디
SELECT ANIMAL_ID from animal_ins
where name is not null
order by ANIMAL_ID

--3 NULL 처리하기
SELECT ANIMAL_TYPE, ifnull(name,"No name") AS "NAME", SEX_UPON_INTAKE 
from ANIMAL_INS
order by animal_id

5) JOIN
--1 없어진 기록 찾기
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME from animal_outs
left outer join ANIMAL_INS on ANIMAL_OUTS.animal_id = ANIMAL_INS.animal_id
where ANIMAL_INS.animal_id is NULL

--2 있었는데요 없었습니다
SELECT ANIMAL_INS.animal_id , ANIMAL_INS.name 
from ANIMAL_INS join ANIMAL_OUTS
on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME

--3 오랜 기간 보호한 동물(1)
SELECT ANIMAL_INS.name , ANIMAL_INS.datetime
from ANIMAL_INS LeFt outer join ANIMAL_OUTS
on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_OUTS.ANIMAL_ID IS null
order by datetime limit 3;