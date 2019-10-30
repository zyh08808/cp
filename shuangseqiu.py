import  random as rd
list1 = ['01','02','03','04','05','06','07','08','09','10','11']
list2 = [12,13,14,15,16,17,18,19,20,21,22]
list3 = [23,24,25,26,27,28,29,30,31,33]
list4 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
t1=input('type')
t2 = input('type')
t3 = input('type')
a1 = rd.sample(list1, t1)
a2 = rd.sample(list2,t2)
a3 =rd.sample(list4,t3)
s = a1+a2+a3
print(a1)
print(a2)
print(a3)
print(s)
