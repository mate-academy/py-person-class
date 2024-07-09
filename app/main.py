class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def set_atr(key: str, item: dict, keys: list) -> None:
    if (key in keys) and item[key]:
        setattr(
            Person.people[item["name"]],
            key,
            Person.people[item[key]]
        )


def create_person_list(people: list) -> list:
    people_instances = []
    for item in people:
        people_instances.append(Person(item["name"], item["age"]))
    for item in people:
        keys = item.keys()
        set_atr("wife", item, keys)
        set_atr("husband", item, keys)

    return people_instances
