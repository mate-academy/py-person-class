class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person.get("name"), person.get("age")))

    for i in range(len(people)):
        wife_name = people[i].get("wife")
        husband_name = people[i].get("husband")
        if wife_name is not None:
            result[i].wife = Person.people.get(wife_name)
        elif husband_name is not None:
            result[i].husband = Person.people.get(husband_name)

    return result
