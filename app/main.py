class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({f"{name}": self})

    def add_wife(self, wife_name: str = None) -> None:
        wife = Person.people.get(wife_name)
        if wife:
            self.wife = wife
            self.wife.husband = self

    def add_husband(self, husband_name: str = None) -> None:
        husband = Person.people.get(husband_name)
        if husband:
            self.husband = husband
            self.husband.wife = self


def create_person_list(people: list) -> list:

    # Create person instances
    result = [Person(person["name"], person["age"]) for person in people]

    # Establish relationships
    for person in people:
        person_instance = Person.people[person["name"]]
        if person.get("wife"):
            person_instance.add_wife(person["wife"])
        if person.get("husband"):
            person_instance.add_husband(person["husband"])

    return result
