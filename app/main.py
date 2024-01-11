class Person:
    people = {}     # { name -> Person }

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        if hasattr(self, "wife"):
            return f"Person| {self.name} /{self.age} wife= {self.wife.name}"
        elif hasattr(self, "husband"):
            return f"Person| {self.name} /{self.age} husb= {self.husband.name}"
        else:
            return f"Person| {self.name} /{self.age}"


def create_person_list(people: list) -> list:
    person_list = []
    # filling list of <People> instances
    for person in people:
        human = Person(person["name"], person["age"])
        person_list.append(human)
    # check & create relations <wife/husband> for instances
    for person in people:
        name = person["name"]
        if person.get("wife"):
            Person.people[name].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[name].husband = Person.people[person["husband"]]

    return person_list
