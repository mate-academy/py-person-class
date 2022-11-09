class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:

    arr = []
    for line in people:
        arr.append(Person(line["name"], line["age"]))

    for obj in people:
        for human in arr:
            if obj["name"] == human.name:
                for human_family in arr:
                    if obj.get("wife") == human_family.name:
                        human.wife = human_family
                    if obj.get("husband") == human_family.name:
                        human.husband = human_family
    return arr
