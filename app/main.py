class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        persons.append(Person(person["name"], person["age"]))

    for person in people:
        person_object = Person.people[person["name"]]
        if person.get("wife") is not None:
            wife_object = Person.people[person["wife"]]
            person_object.wife = wife_object
        if person.get("husband") is not None:
            husband_object = Person.people[person["husband"]]
            person_object.husband = husband_object
    return persons


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
