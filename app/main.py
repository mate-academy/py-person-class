class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(name=person["name"], age=person["age"])
                   for person in people]

    for person in people:
        human = Person.people[person["name"]]

        wife_name = person.get("wife")
        if wife_name:
            human.wife = Person.people.get(wife_name)

        husband_name = person.get("husband")
        if husband_name:
            human.husband = Person.people.get(husband_name)

    return person_list
