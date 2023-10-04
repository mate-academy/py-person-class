class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for index, person in enumerate(people):
        wife = person.get("wife")
        if wife:
            person_list[index].wife = Person.people.get(wife)
        husband = person.get("husband")
        if husband:
            person_list[index].husband = Person.people.get(husband)
    return person_list



