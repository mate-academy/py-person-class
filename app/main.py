class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        new_person = Person(person_dict.get("name"), person_dict.get("age"))
        if "wife" in person_dict and person_dict.get("wife"):
            new_person.wife = person_dict.get("wife")
        elif "husband" in person_dict and person_dict.get("husband"):
            new_person.husband = person_dict.get("husband")
        person_list.append(new_person)
    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people.get(person.wife)
        elif hasattr(person, "husband"):
            person.husband = Person.people.get(person.husband)
    return person_list
