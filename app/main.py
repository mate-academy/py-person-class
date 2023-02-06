class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_instances = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        instance = Person.people[person["name"]]

        if check_marital_status(person) == "married":
            if check_gender(person) == "man":
                instance.wife = Person.people[person["wife"]]
            else:
                instance.husband = Person.people[person["husband"]]

    return list_of_instances


def check_gender(person: dict) -> str:
    return "man" if "wife" in person else "woman"


def check_marital_status(person: dict) -> str:
    husband = person.get("husband")
    wife = person.get("wife")

    return "married" if wife or husband is not None else "unmarried"
