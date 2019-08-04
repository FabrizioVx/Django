#Codigo para Realizar las los ejemplos de video 12 y 13



from datetime import date
personas = [	
	{
	'email' :'avilia.consuelo@utec.edu.pe',
	'password':'Avilia1402',
	'first_name':'Avilia',
	'last_name':'Auqui',
	'bio':'Avilia Consuelo Auqui Maraví es una ama de casa de la Familia Vásquez Auqui, actualmente tiene 49 años de edad, es originaria de Concepción y actualmente vive en Lima-Perú.',
	'birthday':date(1969,2,14),
	'country':'Huancayo',
	'is_admin':True
	},
	{
	'email' :'luis.vasquez@gmail.com',
	'password':'Luis0210',
	'first_name':'Fabrizio',
	'last_name':'Vásquez',	
	'bio':'Luis Vásquez señor de 50 años de edad , actualmente vive en Lima La Victoria.',
	'birthday':date(1967,10,2),
	'country':'Huancayo',
	'is_admin':True
	}
	]	


from posts.models import User

for data in personas:
	obj = User(**data)
	obj.save()
	print(obj.first_name,':',obj.email,':',obj.country,":",obj.birthday)


--------------------------------------------------------------------------------------------------------------------->


def __str__(self):
	return self.first_name

for u in user:
	print(u.first_name,':',u.email,':',u.birthday,':',u.country,':',u.password)
