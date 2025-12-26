class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    persons = [Person(data.get("name"), data.get("age")) for data in people]

    for data in people:
        spouse_name = data.get("wife") or data.get("husband")
        if spouse_name is None:
            continue
        spouse_key = "wife" if data.get("wife") else "husband"
        person = Person.people.get(data.get("name"))
        spouse = Person.people.get(spouse_name)
        setattr(person, spouse_key, spouse)

    return persons
