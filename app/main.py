class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in person_list:

        for human in people:

            if person.name == human["name"]:
                wife = human.get("wife")
                husband = human.get("husband")

                if wife:
                    person.wife = Person.people[wife]
                elif husband:
                    person.husband = Person.people[husband]

    return person_list
