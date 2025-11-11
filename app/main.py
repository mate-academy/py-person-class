class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people_list: list) -> list:
    person_list = []
    for person in people_list:
        new_person = Person(person["name"], person["age"])
        Person.people[person["name"]] = new_person
        person_list.append(new_person)

    for pos, person in enumerate(person_list):
        if people_list[pos].get("wife"):
            person.wife = Person.people[people_list[pos]["wife"]]
            person.wife.husband = person
        if people_list[pos].get("husband"):
            person.husband = Person.people[people_list[pos]["husband"]]
            person.husband.wife = person

    return person_list
