class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for dict_people in people:
        result.append(Person(dict_people["name"], dict_people["age"]))

    for dict_people in people:
        person = Person.people[dict_people["name"]]

        if dict_people.get("wife"):
            person.wife = Person.people[dict_people["wife"]]

        if dict_people.get("husband"):
            person.husband = Person.people[dict_people["husband"]]

    return result
