class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = Person(human["name"], human["age"])
        if "wife" in human and human["wife"] is not None:
            person.wife = human["wife"]
        if "husband" in human and human["husband"] is not None:
            person.husband = human["husband"]
        persons.append(person)

    for person in persons:
        if hasattr(person, "wife"):
            for other_person in persons:
                if other_person.name == person.wife:
                    person.wife = other_person
                    break

        if hasattr(person, "husband"):
            for other_person in persons:
                if other_person.name == person.husband:
                    person.husband = other_person
                    break
    return persons
