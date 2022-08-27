-- SQLite
SELECT last_name || first_name 이름, age,country,phone,balance
from users
limit 5;

select length(last_name),last_name
from users
limit 5;

select first_name, phone,REPLACE(phone,'-','')
from users
limit 5; 

SELECT mod(5,2)
from users
LIMIT 1; --앞숫자 뒷숫자를 나눈 나머지

select Ceil(5.2)
from users
limit 1; -- 올림

SELECT floor(5.2)
from users
limit 1 ; --내림

SELECT round(5.3432,2)
from users
limit 1; --반올림, n째자리까지

select power(3,2)
from users
limit 1; -- 숫자1의 숫자2 제곱

SELECT sqrt(4)
from users
limit 1; --제곱근
