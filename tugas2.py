print ('tugas program untuk menentukan bilangan terbesar ')

print ('masukkan 3 bilangan yang diinginkan!')
a=int(input('bilangan 1 = '))
b=int(input('bilangan 2 = '))
c=int(input('bilangan 3 = '))

if a>b and a>c:
    if b>c:
        print (a, 'adalah bilangan terbesar dari 3 bilangan yang di input')
    else:
        print (a, 'adalah bilangan terbesar dari 3 bilangan yang di input')
elif b>a and b>c:
    if a>c:
        print (b, 'adalah bilangan terbesar dari 3 bilangan yang di input')
    else:
        print (b, 'adalah bilangan terbesar dari 3 bilangan yang di input')
else:
    if a>b:
        print (c, 'adalah bilangan terbesar dari 3 bilangan yang di input')
    else:
        print (c, 'adalah bilangan terbesar dari 3 bilangan yang di input')
