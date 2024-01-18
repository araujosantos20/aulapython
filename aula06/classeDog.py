# criação da classe dog que dará origem a vários dogs
class Dog:
    # criação da função init, que é responsável 
    # por dar início o objeto que será criado.
    # está sendo peido o nome e a idade do dog no 
    # momento em que ele é criado.
    # usamos o termo self para fazer uma referência
    # a própria classe. portanto, quando criar o dog
    #  e passar o nome e a idade, elas pertencerão à
    # classe dog
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def dataDog(self):
        print(self.name)
        print(self.age)
    def sit(self):
        print("sentou")
    def roll_over(self):
        print("rolou")
    
