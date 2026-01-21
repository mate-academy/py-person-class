class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    person_list = []
    for person in people:
        new_person = Person.people.get(person["name"])
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name:
            setattr(new_person, "wife", Person.people.get(wife_name))

        if husband_name:
            setattr(new_person, "husband", Person.people.get(husband_name))
        person_list.append(new_person)
    return person_list
