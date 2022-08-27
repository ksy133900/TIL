-- SQLite
1. select count(*) from healthcare;

2. select max(age),min(age) from healthcare;

3. select max(height),max(weight),min(height),min(weight) from healthcare;

4. select count(*) from healthcare where height BETWEEN 160 and 170;

select * from healthcare where is_drinking = 1 ORDER by waist DESC limit 5;

select count(*) from healthcare where is_drinking = 1 and va_left >= 1.5 and va_right >= 1.5;

select count(*) from healthcare where blood_pressure < 120;

select avg(waist) from healthcare where blood_pressure > 120

select avg(height),avg(weight) from healthcare where gender = 1;


select id,height,weight from healthcare ORDER by height DESC limit 1 offset 1;

select count(*) from healthcare where weight*10000/(height*height) >= 30; 

select id, weight*10000/(height*height) as bmi from healthcare where smoking = 3 order by weight*10000/(height*height) DESC limit 5;

select id,height,weight from healthcare ORDER by height DESC, weight desc limit 1 offset 1; 

select count(*) as wear_glasses from healthcare where ((va_left = 2.0 and va_right <= 0.5) or (va_right = 2.0 and va_left <= 0.5));

select id,weight from healthcare where smoking = 2 order by height desc limit 1 offset 3;

음주를 하지 않는 사람들의 몸무게와 키의 평균을 구하고 더한 값을 출력.

select avg(weight) + avg(height) from healthcare where is_drinking = 0;
select avg(weight) from healthcare where is_drinking = 0;
select avg(height) from healthcare where is_drinking = 0;

select * From (select sum(weight), sum(height) from healthcare where is_drinking = 0 ORDER by weight desc, height desc) group by col limit 5;




SELECT avg(age) FROM healthcare WHERE (weight >= 130 and smoking = 3) or (weight >= 130 and is_drinking = 1);

select avg(age) from healthcare where (smoking = 3 or is_drinking) = 1 ORDER by weight desc offset 99;

SELECT weight FROM healthcare group order by weight DESC limit 1 OFFSET 99 
SELECT avg(age) FROM healthcare WHERE (weight >= 130 and smoking = 3) or (weight >= 130 and is_drinking = 1);