class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for one_human in people:
        Person(one_human["name"], one_human["age"])

    for name, person in Person.people.items():
        print(f"keys - {name}, values - {person}")

        for some_human in people:
            if some_human["name"] is not name:
                continue
            if "wife" in some_human.keys() and some_human["wife"] is not None:
                person.wife = Person.people[some_human["wife"]]
            if "husband" in some_human.keys() and some_human["husband"] \
                    is not None:
                person.husband = Person.people[some_human["husband"]]
        result.append(person)

    return result


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
