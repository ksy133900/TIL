-- SQLite
create table users (
    first_name TEXT not null,
    last_name text not null,
    age int not null,
    country text not null,
    phone text not null,
    balance int not NULL
)

-- users 테이블에서 age가 30이상인 유저의 모든 컬럼 정보 출력
select * from users where age >= 30;

-- users 테이블에서 age가 30이상인 유저의 이름만 출력
select first_name from users where age >= 30;

-- users 테이블에서 age가 30 이상, 성이 ‘김’인 사람의 나이와 이름만 조회
select first_name, age from users where (age >= 30 and last_name = '김');

-- users 테이블의 레코드 총 개수를 조회
select count(*) from users;

-- 30살 이상인 사람들의 평균 나이 조회
select avg(age) from users where age >= 30;

-- 계좌 잔액(balance)이 가장 높은 사람과 액수 조회
select first_name,max(balance) from users;

-- 나이가 30 이상인 사람의 계좌 평균 잔액을 조회
select avg(balance) from users where age >= 30;

-- users 테이블에서 나이가 20대인 사람만 조회
select * from users where age between 20 and 29; 


-- users 테이블에서 지역 번호가 02인 사람만 조회
select * from users where age like '2%_';

--users 테이블에서 이름이 ‘준’으로 끝나는 사람만 조회
SELECT * from users where first_name like '%준';

-- users 테이블에서 중간 번호가 5114인 사람만 조회
SELECT * FROM users WHERE phone like '%-5114-%';

--. users 에서 나이 순으로 오름차순 정렬하여 상위 10개만 조회
select * from users ORDER by age  ASC limit 10

--. users 에서 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회
SELECT * from users order by age , last_name asc limit 10;

--계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회
select last_name,first_name from users ORDER by balance DESC limit 10;