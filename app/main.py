class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_list: list) -> list:
    persons = []
    for d in people_list:
        name = d["name"]
        age = d["age"]
        person = Person(name, age)
        persons.append(person)
    for d in people_list:
        person = Person.people[d["name"]]
        if "wife" in d and d["wife"] is not None:
            spouse_name = d["wife"]
            if spouse_name in Person.people:
                person.wife = Person.people[spouse_name]
            else:
                person.wife = None  
        if "husband" in d and d["husband"] is not None:
            spouse_name = d["husband"]
            if spouse_name in Person.people:
                person.husband = Person.people[spouse_name]
            else:
                person.husband = None
    return persons
