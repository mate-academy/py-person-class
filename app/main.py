class Person:
    people = [] 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self   
def create_person_list(people):
    result = []
    for p in people:
        person = Person(p["name"], p["age"])
        result.append(person)
    for p in people:
        if p.get("wife") != None:
            person.wife = Person.people[p["wife"]]  
        if p.get("husband") is not None:
            person.husband = Person.people[p["husband"]] 
