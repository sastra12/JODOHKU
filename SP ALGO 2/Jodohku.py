import random

print("+++Aplikasi Biro Jodoh+++")
print("1.Cocokan secara random")
print("2.Cccokan dengan banyak calon")
print("3.Cocokan nama dan juga zodiak")

menu1=input("Masukan pilihan: ")
if(menu1=="1"):
    a= input("Masukan nama cowok: ")
    b= input("Masukan nama cewek: ")
    print("Nama cowok: ",a)
    print("Nama cewek: ",b)
    kondisi=True
    while(kondisi):
        x=input("Apakah nama pasangan sudah benar ? y/n: ")
        if(x=="y"):
            kondisi=False
    hasil= random.randrange(0,100)
    if(hasil>80):
        print("Ndang Rabi")
    elif(hasil>60):
        print("Yakin")
    elif(hasil>40):
        print("Pikir-pikir")
    elif(hasil>20):
        print("Putus Aja")
    else:
        print("Cari Lagi")
    print("Presentasi kecocokan anda adalah: ",hasil,"%")

elif(menu1=="2"):
    cewek = []
    nilai=[]
    hasil=0
    z=[]
    a = int(input("Masukan jumlah calon perempuan: "))
    cowok1= input("Masukan nama cowok: ")
    for x in range (a):
        cewek1=input("Input Nama Cewek: ")
        cewek.append(cewek1)
    for y in(cewek):
        acak= random.randrange(0,100)
        hasil=hasil+acak
        nilai.append(hasil)
        hasil=0
    result=zip()
    result=list(zip(cewek,nilai))
    print(result)
    for xn in range(len(result)):
        print("nilai",result[xn][1],"% dipunyai oleh",result[xn][0])
        u=result[xn][1],result[xn][0]
        z.append(u)
        q=max(z)
    print(cowok1,"cocok dengan",q[1],"dengan nilai",q[0],"%")

elif(menu1=="3"):
    hasil=0
    cwok=input("Masukan nama cowok: ")
    zodiak_cowok=input("Masukan Zodiak cowok: ")
    cwek=input("Masukan nama cewek: ")
    zodiak_cewek=input("Masukan Zodiak cewek: ")
    nama= random.randrange(0,50)
    zodiak= random.randrange(0,50)
    hasil=hasil+nama+zodiak
    print(hasil,"%")
    if(hasil>80):
        print("Ndang Rabi")
    elif(hasil>60):
        print("Yakin")
    elif(hasil>40):
        print("Pikir-pikir")
    elif(hasil>20):
        print("Putus Aja")


