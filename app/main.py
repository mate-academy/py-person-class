class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict[str, str | int | None]]) -> list:
    person_list = []
    [
        person_list.append(Person(human["name"], human["age"]))
        for human in people
    ]
    for index_person, person in enumerate(people):
        if "wife" in person and person.get("wife") is not None:
            person_list[index_person].wife\
                = Person.people.get(person.get("wife"))
        if "husband" in person and person.get("husband") is not None:
            person_list[index_person].husband\
                = Person.people.get(person.get("husband"))
    return person_list
