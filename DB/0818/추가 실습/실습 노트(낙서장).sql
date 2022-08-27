-- SQLite

1
select smoking, count(*) from healthcare GROUP by smoking ;
2
select is_drinking, count(*) from healthcare GROUP by is_drinking ;
3
select is_drinking, count(*) from healthcare where blood_pressure >= 200 GROUP by is_drinking;
4
SELECT sido, count(*) from healthcare group by sido having count(*) >= 50000;
5
select height , count(*) from healthcare GROUP by height order by count(*) DESC limit 5;

6
select weight, height , count(*) from healthcare GROUP by height,weight order by count(*) DESC limit 5;
having ;
7
select is_drinking, avg(waist), count(*) from healthcare where is_drinking !='' group by is_drinking;


8
select round(avg(va_left),2) as '평균 왼쪽 시력', round(avg(va_right),2) as '평균 오른쪽 시력' from healthcare group by gender;
9
select age, avg(height) as '평균 키' , avg(weight) as '평균 몸무게' from healthcare 
group by age having avg(height) >= 160 and avg(weight) >= 60;

10
select is_drinking, smoking, avg(weight/(height*0.01)/(height*0.01)) from healthcare
where is_drinking !='' and smoking !='' GROUP by is_drinking, smoking;