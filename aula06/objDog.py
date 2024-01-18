from classeDog import Dog
# para criar o objeto, utilizamos a variável pastor e ralizamos o processo de instanciação da classe dog.
# foi passado o nome e a idade 
pastor = Dog("bob", 2)
# acessamos o método data.dog que mostra os dados do cachorro.
pastor.dataDog()
pastor.sit()
pastor.roll_over()
print(pastor.__class__)
print(pastor.__dict__)