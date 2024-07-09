class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = {}
        self.husband = {}
        self.people[self.name] = self


def remove_atr(instance: Person, key: str) -> None:
    if (hasattr(instance, key)
            and not isinstance(getattr(instance, key), Person)):
        delattr(instance, key)


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
        for instance in people_instances:
            remove_atr(instance, "wife")
            remove_atr(instance, "husband")

    return people_instances
