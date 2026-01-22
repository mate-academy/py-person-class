class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=one_person["name"], age=one_person["age"])
        for one_person in people
    ]

    for one_person in people:
        person_name = Person.people[one_person.get("name")]
        if one_person.get("wife"):
            person_name.wife = Person.people[one_person.get("wife")]
        if one_person.get("husband"):
            person_name.husband = Person.people[one_person.get("husband")]

    return person_list
