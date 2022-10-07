class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    lst = []
    for pers in people:
        person = Person(
            name=pers["name"],
            age=pers["age"]
        )

        if pers.get("wife") is not None:
            person.wife = pers.get("wife")

        if pers.get("husband") is not None:
            person.husband = pers.get("husband")

        lst.append(person)

    for pers in lst:
        if hasattr(pers, "wife"):
            pers.wife = pers.people[pers.wife]

        if hasattr(pers, "husband"):
            pers.husband = pers.people[pers.husband]

    return lst
