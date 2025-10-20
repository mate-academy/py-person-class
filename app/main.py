class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for human in people:
        Person(human["name"], human["age"])
    for human in people:
        person_obj = Person.people[human["name"]]
        wife_name = human.get("wife")
        husband_name = human.get("husband")

        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]

    return [Person.people[d["name"]] for d in people]
