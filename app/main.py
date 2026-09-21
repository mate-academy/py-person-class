class Person:
    people = {}
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_data):
    person_list = [Person(person["name"], person["age"]) for person in people_data]
    
    for person_dict, person_instance in zip(people_data, person_list):
        if person_dict.get("wife"):
            person_instance.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person_instance.husband = Person.people[person_dict["husband"]]
    
    return person_list
