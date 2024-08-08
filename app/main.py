class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_info in people:
        Person(person_info["name"], person_info["age"])
    for person_info in people:
        person = Person.people[person_info["name"]]
        if person_info.get("wife") in (None, "None"):
            if hasattr(person, "wife"):
                delattr(person, "wife")
        elif person_info.get("wife") not in (None, "None"):
            person.wife = Person.people[person_info["wife"]]

        if person_info.get("husband") in (None, "None"):
            if hasattr(person, "husband"):
                delattr(person, "husband")
        elif person_info.get("husband") not in (None, "None"):
            person.husband = Person.people[person_info["husband"]]
    return list(Person.people.values())
