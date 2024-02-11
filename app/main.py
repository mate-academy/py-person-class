class Person:
    people = {}
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    for person in people:
        if person['name'] not in Person.people:
            Person(person['name'], person['age'])
    
    for person in people:
        if 'wife' in person and person['wife']:
            Person.people[person['name']].wife = Person.people[person['wife']]
        elif 'husband' in person and person['husband']:
            Person.people[person['name']].husband = Person.people[person['husband']]
    
    return list(Person.people.values())

people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
