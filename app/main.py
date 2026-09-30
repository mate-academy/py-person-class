class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_current = Person(name, age)
        result.append(person_current)

    for person in people:
        person_current = Person.people.get(person["name"])
        if person_current:
            if person.get("wife"):
                wife_name = person["wife"]
                person_current.wife = Person.people.get(wife_name)
            elif person.get("husband"):
                husband_name = person["husband"]
                person_current.husband = Person.people.get(husband_name)
    return result
