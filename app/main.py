class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}  # Reset the people dictionary
    for person in people:
        if person["name"] not in Person.people:
            Person(person["name"], person["age"])

    sorted_people = sorted(Person.people.values(), key=lambda x: x.name)

    for person in people:
        if "wife" in person and person["wife"]:
            sorted_people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            sorted_people[person["name"]].husband = \
                Person.people[person["husband"]]

    return sorted_people


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
