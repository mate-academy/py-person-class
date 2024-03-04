class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for i in range(len(people)):
        current_person = people[i]
        wife_name = current_person.get("wife")
        husband_name = current_person.get("husband")

        target_person = Person.people[current_person.get("name")]

        if wife_name is not None:
            target_person.wife = Person.people[wife_name]
        elif husband_name is not None:
            target_person.husband = Person.people[husband_name]

    return list(Person.people.values())
