class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)

        if "wife" in person_info and person_info["wife"] is not None:
            person.wife = person_info["wife"]
        elif "husband" in person_info and person_info["husband"] is not None:
            person.husband = person_info["husband"]

        result.append(person)

    for person in result:
        if hasattr(person, "wife") and person.wife in Person.people:
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband") and person.husband in Person.people:
            person.husband = Person.people[person.husband]

    return result
