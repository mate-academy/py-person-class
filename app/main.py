class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(list_people: list) -> list:
    [Person(person["name"], person["age"]) for person in list_people]
    for person in list_people:
        if person.get("wife") is not None:
            person_name = person["wife"]
            current_person = Person.people[person.get("name")]
            current_person.wife = Person.people[person_name]
        elif person.get("husband") is not None:
            person_name = person["husband"]
            current_person = Person.people[person.get("name")]
            current_person.husband = Person.people[person_name]
    return list(Person.people.values())
