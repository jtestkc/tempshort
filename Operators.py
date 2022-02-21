xy, zx , cx , za , ds , op = 1500, 1434 , 1612 , 10.0022 , 8771 , "5678"
xz = xy * zx #Multiplication
xc = zx + cx #Addition
vc = xy - zx #subtraction
bc = cx / xy #DIVIDE
xy += 700 #assigning
zx = cx % za #Modulus
hehe = za + ds #type conversion implicit
op = int(op) #type conversion explicit
lp = ds + op
print(xz,'\n',vc,'\n' ,bc,'\n' ,xy, '\n', '\n', hehe ,"HEHE is of type:",type(hehe),'\n',lp,"LP is of type:",type(lp))
bin(22)