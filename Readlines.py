f=open("D:\\VScode\\Python\\copy.txt",'r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)