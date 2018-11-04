print('Merhaba, Django girls!')
name='irem'
if name== 'Ayşe':
   print('Selam Ayşe!')
elif name=='Zeynep':
   print('Selam Zeynep!')
else:
   print('Selam yabancı!')


volume=101
if volume<20:
    print("Çok sessiz.")
elif 20<= volume <40:
    print("Güzel bir fon müziği")
elif 40<= volume <60:
    print("Harika, her notayı duyabiliyorum")
elif 60<= volume <80:
     print("Parti başlasın")
elif 80<= volume<100:
     print("Biraz gürültülü!")
else:
     print("Kulalarım ağrıyor!:(")
#Çok yüksek ya da çok düşük olduğunda ses eviyesini değiştirme
if volume<20 or volume>80:
  volume=50
  print("thats better")
  print(volume)


def hi():
   print('Merhaba!')
   print('Nasılsın?')

hi()



def selam (name):
	if name== 'ayşe':
	     	print('merhaba ayşe')
	elif name=='zeynep':
		print('merhaba zeynep')
	else: 
		print ('merhaba yabancı')
selam(name)
selam("zeynep")

#selam() dedigimde calismaz

girls=['seda','gül','irem','ayşe','melis']

def hi(name):
    print('Merhaba ' + name + '!')

girls = ['Seda', 'Gül', 'Pınar', 'Ayşe', 'Sen']
for name in girls:
    hi(name)
    print('Sıradaki kız') 

for i in range(1,6):
	print(i)
     
