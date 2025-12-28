class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = \
        [Person(pers.get("name"), pers.get("age")) for pers in people]

    for pers in people:
        person_instance = Person.people.get(pers.get("name"))
        wife_name = pers.get("wife")
        husband_name = pers.get("husband")
        if wife_name:
            person_instance.wife = Person.people.get(wife_name)
        if husband_name:
            person_instance.husband = Person.people.get(husband_name)

    return person_list
