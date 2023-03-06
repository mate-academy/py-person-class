class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[Person]) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person.get("name"), person.get("age")))
    for person in people:
        class_people_name = Person.people.get(person.get("name"))
        if "wife" in person and person.get("wife") is not None:
            class_people_name.wife = Person.people.get(person.get("wife"))
        elif "husband" in person and person.get("husband") is not None:
            class_people_name.husband =\
                Person.people.get(person.get("husband"))
    return people_list
