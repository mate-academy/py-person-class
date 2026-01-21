class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        obj = Person(person["name"], person["age"])
        partner = "wife" if "wife" in person else "husband"
        setattr(obj, partner, person[partner])
        persons.append(obj)

    for person in persons:
        partner = "wife" if hasattr(person, "wife") else "husband"
        key = getattr(person, partner)
        if key is None:
            delattr(person, partner)
        else:
            obj = Person.people[key]
            setattr(person, partner, obj)
    return persons
