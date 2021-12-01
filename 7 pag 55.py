a=open('C:/Users/Lenovo/Desktop/caratere.txt', 'r')
b=a.read()
c=[]
d=0
a.close()
for i in range(0,len(b)):
    if b[i]=='a' or b[i]=='e' or b[i]=='i' or b[i]=='o' or b[i]=='u' or b[i]=='A' or b[i]=='E' or b[i]=='I' or b[i]=='O' or b[i]=='U':
      c.append(b[i])
      d+=1
c=str(c)
d=str(d)
print(c)
print(d)
e=open('C:/Users/Lenovo/Desktop/vocale.txt', 'w')
e.write(c)
e.close()
f=open( 'C:/Users/Lenovo/Desktop/numarul de vocale.txt',  'w')
f.write(d)
f.close()