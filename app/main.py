class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        if "wife" in person.keys() and person["wife"] is not None:
            wife = Person(person["wife"], 0)
            people_list[index].wife = wife
            wife.husband = people_list[index]
        elif "husband" in person.keys() and person["husband"] is not None:
            husband = Person(person["husband"], 0)
            people_list[index].husband = husband
            husband.wife = people_list[index]

    return people_list
