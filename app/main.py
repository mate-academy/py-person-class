class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for item in people:
        person = Person(item["name"], item["age"])
        person_list.append(person)

    for item in people:
        person = Person.people[item["name"]]

        wife_name = item.get("wife")
        husband_name = item.get("husband")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list
