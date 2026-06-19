class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []

    for i in people:
        name = i["name"]

        person = Person(name, i["age"])
        Person.people[name] = person
        person_list.append(person)

    for i in people:
        current = Person.people[i["name"]]

        wife_name = i.get("wife")
        husband_name = i.get("husband")

        if wife_name:
            current.wife = Person.people[wife_name]

        if husband_name:
            current.husband = Person.people[husband_name]
    return person_list
