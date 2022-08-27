-- SQLite
# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000명
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```
```
156277명
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1 ;
```
```
510689명
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;
```
```
150361명
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 AND va_right >= 2.0;
```
```
2614 명
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare ;
```

```
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람
```sql x = 5 y = 85
SELECT COUNT(*) FROM healthcare WHERE waist >= 5 AND weight <= 85;
```

\### 혈압이 90보다 높고 130보다 낮은 사람 수

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure between 90 AND 130;
```

```sqlite
676159명
```