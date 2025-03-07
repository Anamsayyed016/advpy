# Create:-
# f=open('n1.txt','x')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n1.txt','w')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n1.txt','r')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())


# f=open('n1.txt','a')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('p1.txt','w')
# data="hii"
# f.write(data)
# f.close()

# f=open('p1.txt','w')
# data=['Hi\n','hello\n','welcome\n']
# f.writelines(data)
# f.close()

f=open('p1.txt','a')
data=['Hi\n','hello\n','welcome\n']
f.writelines(data)
f.close()