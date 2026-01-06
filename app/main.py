class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Person.people[self.name] = self


def create_person_list(people: list) -> list:
    need_return = []
    # Person.people.clear()
    for person in people:
        Person.people[person["name"]] = Person(person["name"], person["age"])
        need_return.append(Person.people[person["name"]])
    for person in people:
        if person.get("wife", "dont_have") != "dont_have":
            if not person["wife"] is None:
                Person.people[f"{person["name"]}"].wife = (
                    Person.people)[person["wife"]]
        else:
            if not person["husband"] is None:
                Person.people[f"{person["name"]}"].husband = (
                    Person.people)[person["husband"]]
    # Person.people = {}
    return need_return
