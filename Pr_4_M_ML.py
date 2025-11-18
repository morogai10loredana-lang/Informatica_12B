e1=('Guşan', 'Francesca', 'F',10,10,10) 
e2=('Morogai', 'Loredana', 'F',9,10,10)
e3=('Girlă', 'Lilia', 'F',9,10,10) 
e4=('Covalciuc', 'Ana', 'F',10,10,10) 
e5=('Coban', 'Mihai', 'M',9,7,10)
print('1) nota medie obtinută la sesiune de fiecare elev')

print(e1[:2], 'cu media la teza de', sum(e1[3:])/3)
print(e2[:2], 'cu media la teza de' , sum(e2[3:])/3)
print(e3[:2], 'cu media la teza de', sum(e4[3:])/3)
print(e5[:2], 'cu media la teza de' , sum(e5[3:])/3)


print('2) numele, prenumele elevilor restanțieri')
if((e1[3]<5) or (e1[4]<5) or (e1[5]<5)):
   print(e1[:2])
if ((e2[3]<5) or (e2[4]<5) or (e2[5]<5)):
   print(e2[:2])
if ((e3[3]<5) or (e3[4]<5) or (e3[5]<5)):
   print(e3[:2])
if ((e4[3]<5) or (e4[4]<5) or (e4[5]<5)):
   print(e4[:2])
if ((e5[3]<5) or (e5[4]<5) or (e5[5]<5)):
   print(e5[:2])



print('3) numele, prenumele elevilor eminenti')
if ((e1[3]<5) or (e1[4]<5) or (e1[5]<5)):
   print (e2[:2])
if ((e2[3]<5) or (e2[4]<5) or (e2[5]<5)):
   print (e3[:2])
if ((e3[3]<5) or (e3[4]<5) or (e3[5]<5)):
   print(e4[:2])
if ((e4[3]<5) or (e4[4]<5) or (e4[5]<5)):
   print(e4[:2])
if ((e5[3]<5) or (e5[4]<5) or( e5[5]<5)):
   print(e5[:2])



print('3) numele, prenumele elevilor eminenti')
if ((e1[3]>=9) and (e1[4]>=9) and (e1[5]>=9)):
   print(e1[:2])
if ((e2[3]>=9) and (e2[4]>=9) and (e2[5]>=9)):
   print (e2[:2])
if ((e3[3]>=9) and (e3[4]>=9) and (e3[5]>=9)):
   print(e3[:2])
if ((e4[3]>=9) and (e4[4]>=9) and (e4[5]>=9)):
   print (e4[:2])
if ((e5[3]>=9) and (e5[4]>=9) and (e5[5]>=9)):
   print (e5[:2])