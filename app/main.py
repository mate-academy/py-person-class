class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list[dict]) -> list:
    person_list = []
    for person in people_list:
        person_obj = Person(person["name"], person["age"])
        if "husband" in person:
            if person["husband"] is not None:
                person_obj.husband = person["husband"]
        if "wife" in person:
            if person["wife"] is not None:
                person_obj.wife = person["wife"]
        person_list.append(person_obj)

    for person in person_list:
        if "husband" in person.__dict__:
            setattr(person, "husband", Person.people.get(person.husband))
        if "wife" in person.__dict__:
            setattr(person, "wife", Person.people.get(person.wife))
    return person_list
