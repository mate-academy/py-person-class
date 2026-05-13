class Person:
    people = {}  # class attribute to store all instances by name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self  # register instance on creation

    def set_wife(self, wife: "Person") -> None:
        self.wife = wife

    def set_husband(self, husband: "Person") -> None:
        self.husband = husband


def create_person_list(people_data: list) -> list:
    # First pass: create all Person instances (populates Person.people)
    persons = []
    for data in people_data:
        persons.append(Person(data["name"], data["age"]))

    # Second pass: link wife/husband as actual Person objects
    for data, person in zip(people_data, persons):
        if data.get("wife"):
            wife_person = Person.people[data["wife"]]
            person.set_wife(wife_person)

        if data.get("husband"):
            husband_person = Person.people[data["husband"]]
            person.set_husband(husband_person)

    return persons
