-- SQLite
SELECT count(*) from healthcare

SELECT
    id,
    CASE
        WHEN gender = 1 then '남자'
        when gender = 2 then '여자'
    END
from healthcare
limit 3;


select
    age,
    CASE
        WHEN age <= 18 then '청소년'
        when age <= 30 then '청년'
        when age <= 64 then '중장년'
    END
from healthcare
LIMIT 10;

where SELECT min(age) from healthcare 
---- 나이가 작은
----- 사람의 수
a

select count(*) from users where age = (select min(age) from users);

select count(*) from users
where balance > (select avg(balance) from users); 





