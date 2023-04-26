
lines=["line1\n","line2\n","line3\n"]
text2="\nappended a file"
# with open("D:\\VScode\\Python\\test.txt","w") as file:
with open("D:\\VScode\\Python\\test.txt","w") as f:
    f.writelines(lines)

##to use write write() argument must be str, not list   
#but to use writelines it should be list



#use w for write it will overwrite everything
#use a for append it will append at the last



# f=open['D:\\VScode\\Python\\test.txt','w']
# lines=["line1\n","line2\n","line3\n"]
# f.writelines(lines)
# f.close