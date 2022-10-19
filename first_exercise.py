#########start#####
#########1#########

words=['This','is','my','world']
d={w:len(w) for w in words}
print(d)

#########2######

a=(1,2,3,4)
b=(3,)+a[1:]
print(b)

#########3######

x=(12,234,2,13,456)
x=list(x)
odd=[i for i in x if i%2]
even=[i for i in x if (i not in odd)] 
print(odd,even)

#########4#######

d1={'name':'zhang3','age':12,}
d1.update({'gender':'male'})
d1['profession']='student'
print(d1)

########5########

d2={1:'one',3:'three',5:'five',2:'two'}
print({k:d2[k] for k in sorted(d2.keys())})

#######end#######
