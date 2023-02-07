class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instance_list = []
    for human in people:
        instance = Person(human["name"], human["age"])
        instance_list.append(instance)

    for instance in instance_list:
        for human in people:
            if human["name"] == instance.name:
                if "wife" not in instance.__dict__ and \
                        human.get("wife") is not None:
                    instance.wife = Person.people[human["wife"]]
                if "husband" not in instance.__dict__ \
                        and human.get("husband") is not None:
                    instance.husband = Person.people[human["husband"]]

    return instance_list
