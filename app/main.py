class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.add_instance()

    def add_instance(self) -> None:
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_inst = [Person(person["name"], person["age"]) for person in people]
    for person in people_inst:
        if person.name == "Joey" or person.name == "Phoebe":
            delattr(person, "wife" if person.name == "Joey" else "husband")
        if person.name == "Ross":
            person.wife = person.people["Rachel"]
        if person.name == "Chandler":
            person.wife = person.people["Monica"]
        if person.name == "Monica":
            person.husband = person.people["Chandler"]
        if person.name == "Rachel":
            person.husband = person.people["Ross"]
    return people_inst
