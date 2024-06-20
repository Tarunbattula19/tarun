#expection handling
'''n=int(input())
if n>=0:
    print("yes!! a non-negative number")
else:
    print("no negative number allowed")
'''
#
'''a=int(input())
b=int(input())
try:
    print("a/b=",a/b)
except:
    print("b cannot be done")
print("done execution")'''
#
'''s=(1,2,3)
try:
    s.append(5)
    print(s/0)
except AttributeError:
    print("tuple cant append")
except ZeroDivisionError:
    print("dividing by zero")
except:
    print("some Error come")
'''
#
'''
s=[1,2,3]
try:
    s.append(2)
    print(s)
except AttributeError:
    print("tuple cant append")

else:
    print("some Error come")
'''
#
'''s=(1,2,3)
try:
    s.append(2)
    print(s)
except AttributeError:
    print("tuple cant append")

else:
    print("some Error come")
finally:
    print("code have been run")
'''
#string formatting









