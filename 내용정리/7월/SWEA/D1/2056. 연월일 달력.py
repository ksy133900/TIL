md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for tt in range(T):
    s = input()
    month = int(s[4:6])
    day = int(s[6:8])
    res = "-1"
    if 1<=month and month<=12 and 1<=day and day<=md[month-1]:
    	res = s[0:4]+"/"+s[4:6]+"/"+s[6:8]
    print(f"#{tt+1} {res}")