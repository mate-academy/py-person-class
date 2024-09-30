class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    human_lst = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        current_name = Person.people[human["name"]]
        husband = human.get("husband")
        wife = human.get("wife")

        if husband:
            current_name.husband = Person.people[husband]
        if wife:
            current_name.wife = Person.people[wife]

    return human_lst
