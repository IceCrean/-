l=('9','8','7','6','5','4')
a=['1','2']
b=['0','1']
c=['0','1','2','3']
for y in a:
    for m in b:
        for d in c:
            if d != m and d != y and m !=y:
                if (y == '2' and d !='0' and  m !='0' and d !='3' ) or (y=='1' and d != '3'):
                    print(y+l[0]+l[1]+l[2]+m+l[3]+d+l[4])
