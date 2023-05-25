class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    person_list = []

    for current_person in people:
        person_list.append(Person(current_person["name"],
                                  current_person["age"]))

    for current_person in people:
        name = current_person.get("name")
        wife = current_person.get("wife")
        husband = current_person.get("husband")
        if wife:
            Person.people.get(name).wife = Person.people.get(wife)
        if husband:
            Person.people.get(name).husband = Person.people.get(husband)

    return person_list
