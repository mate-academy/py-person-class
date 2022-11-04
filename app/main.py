class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:

        if "wife" in human and human["wife"] is not None:
            value_of_marriage = human["wife"]
            person = Person(
                human["name"],
                human["age"]
            )
            setattr(person, "wife", value_of_marriage)

        if "husband" in human and human["husband"] is not None:
            value_of_marriage = human["husband"]
            person = Person(
                human["name"],
                human["age"]
            )
            setattr(person, "husband", value_of_marriage)

        if "wife" in human and human["wife"] is None\
                or "husband" in human and human["husband"] is None:
            person = Person(
                human["name"],
                human["age"]
            )

        person_list.append(person)

    for person in person_list:
        if hasattr(person, "wife"):
            setattr(person, "wife",
                    person.__class__.people[getattr(person, "wife")])

        if hasattr(person, "husband"):
            setattr(person, "husband",
                    person.__class__.people[getattr(person, "husband")])

    return person_list
