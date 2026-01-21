class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for result in people:
        Person(result["name"], result["age"])
    for result in people:
        result_people = Person.people[result["name"]]
        if "wife" in result and result["wife"] is not None:
            result_people.wife = Person.people[result["wife"]]

        if "husband" in result and result["husband"] is not None:
            if result["husband"] in Person.people:
                result_people.husband = Person.people[result["husband"]]

    return list(Person.people.values())
