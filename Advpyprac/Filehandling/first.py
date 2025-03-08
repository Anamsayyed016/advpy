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

# f=open('p1.txt','a')
# data=['Hi\n','hello\n','welcome\n']
# f.writelines(data)
# f.close()
# ----------------------------------------------------------------------------
        # READ
# f=open('p1.txt','r')
# data=f.read()
# print(data)

# data=f.read(5)
# print(data)
                    # # know about cusrsor position---tell()
# print(f.tell())

# data=f.readline()
# print(data)

# data=f.readlines()
# print(data)
# =========================================================================================
# x+,w+,a+  

# f=open('n4.txt','x+')

# print(f.readable())
# print( f.writable())
# print( f.closed)

# f=open('n4.txt','r+')

# print(f.readable())
# print( f.writable())
# print( f.closed) 

# f=open('n4.txt','a+')

# print(f.readable())
# print( f.writable())
# print( f.closed) 
# -------------------------------------------------------------------------------------------------

# py support extension-----.py .pyc
# pickling(module)----serialization, unpickling
# json.py----loads and dams--covert py into json
# bite, bitearry, string--support json

# nonsimple obj
# list---str,tuple-----so on------

# import pickle
# pypi.org

# pickle in pypi.org

# binary extension

import pickle 
# f=open('first.dot','ab')

# data=[10,20,30,'ANam']

# pickle.dump(data,f)
# f.close()

f=open('first.dot','rb')

data=pickle.load(f)
print(data)
