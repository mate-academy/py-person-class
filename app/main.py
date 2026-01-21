class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(per["name"], per["age"]) for per in people]

    for index, per in enumerate(people):
        current = person_list[index]

        if per.get("wife"):
            wife = Person.people[per["wife"]]
            current.wife = wife
            if not hasattr(wife, "husband") or wife.husband is None:
                wife.husband = current

        if per.get("husband"):
            husband = Person.people[per["husband"]]
            current.husband = husband
            if not hasattr(husband, "wife") or husband.wife is None:
                husband.wife = current

    return person_list
