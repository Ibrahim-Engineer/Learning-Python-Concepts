people = int(input("how many people are there: "))
i = 0
while i < people:
    i+=1
    person = str(input("Are you a student?: "))
    x = str(input("Name please: "))
    y = str(input("Address please: "))
    z = str(input("City please: "))
    
    
    
    class trial:
        amount_of_people = 0
        def __init__(self, name, address, city):
            self.name = name
            self.address = address
            self.city = city
            trial.amount_of_people +=1
        def __str__(self):
            return ("Name {}, Address {}, City {}".format(self.name, self.address, self.city))
    
    class student(trial):
        def __init__(self, grade):
            self.grade = grade
        def __str__(self):
            return "Grade {}".format(self.grade)
        
        
    if person == "yes":
        g = str(input("what grade are you in: "))
        student(g)
        print(trial(x,y,z))
        print(student(g))
            
    else:    
        person1 = trial(x,y,z,)
        print(person1)
    print(trial.amount_of_people)