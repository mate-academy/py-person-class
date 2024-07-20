class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    print(Person.people)

    for person in people:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            instance.husband = Person.people[person["husband"]]

    result = []

    for person in people:
        result.append(Person.people[person["name"]])

    return result


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
