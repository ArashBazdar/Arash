from op import sub
from op import mul
from op import div
from op import add
from op import divrem

a=float(input("Enter the first number: "))
op=str(input("Enter one of the operation belonging to {+,-,*,/,%} : "))
b=float(input("Enter the first number: "))

if op=='+':
 print(a,"+",b,"=",add(a,b))
if op=='-':
 print(a,"-",b,"=",sub(a,b))
if op=='*':
 print(a,"*",b,"=",mul(a,b))
if op=='/':
 print(a,"/",b,"=",div(a,b))
if op=='%':
 print(a, "%", b, "=", divrem(a, b))
