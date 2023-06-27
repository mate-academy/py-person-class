class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:  # List[dict] -> List[Person]
    for person_dict in people:
        love_key = "husband" if "husband" in person_dict else "wife"
        name = person_dict["name"]
        age = person_dict["age"]

        person = Person(name, age)

        if person_dict[love_key]:
            setattr(person, love_key, person_dict[love_key])

    for person in Person.people.values():
        love_key = "husband" if hasattr(person, "husband") else "wife"

        if hasattr(person, love_key):
            value = getattr(person, love_key)
            setattr(person, love_key, Person.people[value])

    return list(Person.people.values())
