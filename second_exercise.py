from math import *
##################1#################
legs=94
heads=35
soluntion_domain=[[chicken,heads-chicken] for chicken in range(1,heads)]
def func(x):
        return x[0]*2+x[1]*4==legs
solution=list(filter(func,solution_domain))
print(soluntion)


###################2###############

import json
with open('./country.json') as f:
    country_dict=json.load(f)
def func(country_name):
    return (country_name,)+tuple(country_dict[country_name].values())
sort1=list(map(func,sorted(list(country_dict.keys()))))
sort2=sorted(sort1,key=lambda s: s[1])
print(sort1)
print(sort2)

###################3###############
import random 
val=random.randint(1000,9999)
digit_list=list(str(val))
possible_values=[]
for a in digit_list:
    if int(a):
        b_list=digit_list.copy()
        b_list.remove(a)
        for b in b_list:
            c_list=b_list.copy()
            c_list.remove(b)
            for c in c_list:
                d_list=c_list.copy()
                d_list.remove(c)
                possible_values.append(eval(a+b+c+d_list[0]))
print(list(set(possible_values)))

            
  


