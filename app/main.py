class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.husband = None
        self.wife = None
        Person.people[name] = self

    def set_relationships(self, people: dict) -> dict:
        if "wife" in people and people["wife"]:
            self.wife = Person.people[people["wife"]]
        elif "wife" in people:
            if hasattr(self, "wife"):
                del self.wife

        if "husband" in people and people["husband"]:
            self.husband = Person.people[people["husband"]]
        elif "husband" in people:
            if hasattr(self, "husband"):
                del self.husband


def create_person_list(people: list) -> list:
    person_objects = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_objects.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        person.set_relationships(person_data)

    return person_objects
