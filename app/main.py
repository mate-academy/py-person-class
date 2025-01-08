class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def set_spouse(self) -> None:
        if self.wife and isinstance(self.wife, str):
            self.wife = Person.people.get(self.wife)
            if self.wife:
                self.wife.husband = self
        elif self.husband and isinstance(self.husband, str):
            self.husband = Person.people.get(self.husband)
            if self.husband:
                self.husband.wife = self

def create_person_list(people) -> list:
    person_list = []

    for person in people:
        p = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            p.wife = person["wife"]
        elif "husband" in person and person["husband"] is not None:
            p.husband = person["husband"]

        p.set_spouse()

        person_list.append(p)

    return person_list
