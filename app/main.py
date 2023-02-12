class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for i, person in enumerate(people):
        if "wife" in person and person["wife"]:
            setattr(
                person_list[i],
                "wife",
                Person.people.get(person["wife"])
            )
        elif "husband" in person and person["husband"]:
            setattr(
                person_list[i],
                "husband",
                Person.people.get(person["husband"])
            )
    return person_list
