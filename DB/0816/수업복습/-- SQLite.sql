-- SQLite
-- CREATE TALBE classmates (
--     id INTEGER PRIMARY KEY
--     name TEXT
-- );

-- DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT,
age INT,
adress TEXT
);

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

SELECT * FROM classmates;

INSERT INTO classmastes VALUES ('홍길동',30,'서울');

SELECT * FROM classmates;

DROP TABLE classmates;

CREATE TABLE classmates (
    id INTERGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    adress TEXT NOT NULL
);

INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');

SELECT * FROM classmates;

drop table classmates;

CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name text not null,
    age int not null,
    adress text not null
);

create TAble classmates (
    name text not null,
    age int not null,
    adress text not null
);

insert into classmates values ('홍길동', 30, '서울');
insert into classmates values ('김철수', 30, '제주');
insert into classmates values ('이호영', 26, '제주');
insert into classmates values ('박민희', 29, '대구');
insert into classmates values ('최혜영', 28, '전주');

select * from classmates;

select rowid, name from classmates ;

select rowid, name from classmates limit 1;

select rowid, name from classmates limit 1 offset 2;

select * from classmates where adress = '서울';

select DISTINCT AGE FROM classmates;