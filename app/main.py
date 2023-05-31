class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            wife = Person(person["wife"], 0)
            husband = Person(person["name"], person["age"])
            husband.wife = wife
            wife.husband = husband
            people_list.append(husband)
        elif "husband" in person.keys() and person["husband"] is not None:
            husband = Person(person["husband"], 0)
            wife = Person(person["name"], person["age"])
            wife.husband = husband
            husband.wife = wife
            people_list.append(wife)
        else:
            people_list.append(Person(person["name"], person["age"]))

    return people_list
