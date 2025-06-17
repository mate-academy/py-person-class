class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []
    for person in people:
        new_person = Person(name=person["name"], age=person["age"])
        person_list.append(new_person)
    for index, husband in enumerate(person_list):
        if people[index].get("wife", None) is not None:
            for wife in person_list[index + 1:]:
                if people[index].get("wife") == wife.name:
                    wife.husband = husband
                    husband.wife = wife
                    wife.husband = husband

    return person_list
