-- SQLite
SHOW TABLEs

SELECT * from albums ORDER by title DESC limit 5;

select count(*) as '고객 수' from customers

select FirstName as 이름 , LastName as 성 from customers where Country = 'USA';

select count(*) as '송장 수' from invoices where BillingPostalCode is not null;



select * from invoices where BillingPostalCode ISNULL order by InvoiceDate desc limit 5;

SELECT count(*) from invoices where InvoiceDate LIKE '2013%';
select count(*) from invoices where strftime('%Y', InvoiceDate) = '2013';
SELECT InvoiceDate from invoices;

select CustomerId, FirstName, LastName
from customers
where FirstName like 'L%';


select * from customers;
-- 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
-- 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.
SELECT count(*) as '고객 수' , Country as '나라'
from customers group by country ORDER by '고객 수' DESC limit 5;

--11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 
--Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

SELECT ArtistId , maxm(count(*)) from albums
where (SELECT max(ArtistId) from artists);


-- 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 
--`Country` 와 `State`를 기준으로 그룹화해서 
--각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.

select count(*) as '고객 수' , Country , state from customers
where state NOTNULL GROUP by Country , State
ORDER by '고객 수' DESC , Country desc limit 5;

--14. 고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' 
--NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.

select 
    CustomerId,
    CASE
        WHEN 'FAX' isnull then 'X'
        else 'O'
        End As 'FAX 유/무'
from customers
ORDER by CustomerId limit 5;

-- 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.



SELECT
    LastName,
    FirstName,

    cast(strftime('%Y','now') as int) - cast(strftime('%Y',BirthDate) AS int) + 1 AS '나이'
from employees
ORDER by EmployeeId ;

-- 16. 가수(artists) 테이블에서 
-- 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
-- artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.
SELECT Name from artists 
where ArtistId = ( 
    SELECT 
        ArtistId 
    from ( 
        SELECT 
            ArtistId,
            count(*) AS "앨범 수"
        from albums
        GROUP by ArtistId
        order by "앨범 수" DESC
        limit 1
    )
);

 -- 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
select Name
from genres
where GenreId = (
    SELECT GenreId
    from (
        SELECT
            GenreId,
            count(*) AS "개수"
        from tracks
        GROUP by GenreId
        order by "개수"
        LIMIT 1
    )
);
