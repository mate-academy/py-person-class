class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    # person_list = []

    pers_list = [Person(info.get("name"), info.get("age")) for info in people]

    # for person_info in people:
    #     name = person_info.get("name")
    #     age = person_info.get("age")

    #     person = Person(name, age)
    #     person_list.append(person)

    for info in people:
        current_person = Person.people[info.get("name")]

        if info.get("wife"):
            current_person.wife = Person.people.get(info.get("wife"))

        if info.get("husband"):
            current_person.husband = Person.people.get(info.get("husband"))

    return pers_list
