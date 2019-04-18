#Authored by osman ceylan Desingne coming soon?Mb not(please dont believe that)
#This program licanced by nothink.It means no licance bro because im good boy and i dont angry if you steal or fuck it(How availbe)
#This program find prime numbers.Certainlt cant find all because there is no-limited prime numbers.
#I dont take response because you try very big numbers and fuck your PC.
#I'm also worriying about that please send mail which number your PC fucked up(joking)
def girilensayı():
    D=0
    while D==0:
        try:
            sayı=int(input(x))
            if sayı<=0:
                print("Sıfırdan büyük sayı girmelisin")
            if sayı>10000:
                print ("10000 den buyuk sayılar programın çok uzun sürmesine neden olur")
            if sayı>0 and sayı<10000:
                D=1
        except ValueError:
            print ("!!Lütfen bir sayı giriniz!!")
    return sayı

A=[]
B=[]
def asal():
    a=3
    b=3
    c=11
    t=0
    while c<sayı:
        t=0
        while a<c:
            while b<(c/2):
                if a*b==c:
                    t=t+1
                b=b+2
            b=3
            a=a+2
        if t==0:
            A.append(c)
        a=3
        b=3
        c=c+2
    A.extend([2,3,5,7])
    A.sort()
    for i in range(0,len(A)-2):
        if A[i+1]==A[i]+2:
            B.append((A[i],A[i+1]))
F=0
while F==0:
    try:
        soru=int(input("Asal sayı kontrolü için 1 giriniz \nAsal sayıları listelemek için 2 giriniz \nTercihiniz: "))
        if soru==1 or soru==2:break
        else:
            print ("Lütfen 1 veya 2 giriniz")
    except ValueError:
        print ("Lütfen 1 ve 2 yi kullanın")
if soru==1:
    x="Aramak istediğiniz sayı: "
    sayı=girilensayı()
    asal()
    if A.count(sayı)>=1:
        print ("Bu sayı asal bir sayı")
    elif A.count(sayı)==0:
        print ("Bu sayı asal bir sayı değildir")
elif soru==2:
    x="Limit sayı: "
    sayı=girilensayı()
    asal()
    print ("Asal sayılar:\n",A,"\nİkiz asal sayılar:\n",B)
    
    



