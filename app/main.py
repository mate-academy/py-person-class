class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for pupil in people:
        name = pupil["name"]
        age = pupil["age"]
        Person(name, age)

    for pupil in people:
        person = Person.people[pupil["name"]]

        wife_name = pupil.get("wife")
        husband_name = pupil.get("husband")

        if wife_name is not None and wife_name in Person.people:
            setattr(person, "wife", Person.people[wife_name])

        if husband_name is not None and husband_name in Person.people:
            setattr(person, "husband", Person.people[husband_name])

    return list(Person.people.values())
