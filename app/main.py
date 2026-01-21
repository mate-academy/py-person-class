class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

def create_person_list(peoples: list) -> list:
    person_list = []
    Person.people = {}
    for person in peoples:
        newperson = Person(person["name"], person["age"])
        person_list.append(newperson)
        Person.people[person["name"]] = newperson

    for person in peoples:
        newperson = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            newperson.wife = Person.people[person["wife"]]
            newperson.wife.husband = newperson
        elif "husband" in person and person["husband"]:
            newperson.husband = Person.people[person["husband"]]
            newperson.husband.wife = newperson
    return person_list

people1 = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
]

people2 = [
    {"name": "Chandler", "age": 31, "wife": "Monica"},
    {"name": "Monica", "age": 32, "husband": "Chandler"},
]

list1 = create_person_list(people1)
list2 = create_person_list(people2)

print(Person.people)