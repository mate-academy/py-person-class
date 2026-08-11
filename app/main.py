class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = []
    count = 1
    for person in people:
        if "wife" in person:
            new_name = f"person{count}"
            new_name = Person(name=person["name"], age=person["age"])
        else:
            new_name = Person(name=person["name"], age=person["age"])
        new_list.append(new_name)
        count += 1

    for person in people:
        current = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            current.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            current.husband = Person.people[person["husband"]]

    return new_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
