class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(entry.get("name"), 
                          entry.get("age")) for entry in people]
    for entry in people:
        person = Person.people.get(entry.get("name"))
        spouse_name = entry.get("wife") or entry.get("husband")
        if spouse_name:
            setattr(person, "wife" if entry.get("wife") else "husband", 
                    Person.people.get(spouse_name))
    return person_list
