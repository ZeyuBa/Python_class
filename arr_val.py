arr=[1,2,5,5,6,8,8,12,35]

val=8

if val in arr:
    print([arr.index(val),len(arr)-list(reversed(arr)).index(val)-1])
else:
    print([-1,-1])
