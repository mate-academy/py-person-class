class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict.get("name")
        age = person_dict.get("age")
        if name is not None and age is not None:
            person = Person(name, age)
            person_list.append(person)

    for person in people:
        name = person.get("name")
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            Person.people.get(name).wife = Person.people.get(wife)
        if husband:
            Person.people.get(name).husband = Person.people.get(husband)

    return person_list
