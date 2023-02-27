class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self
    pass

    def create_person_list(people: list) -> list:
        person_list = []
        for human in people:
            human["name"] = Person(human["name"], human["age"])
            person_list.append(human["name"])
        for human in people:
            if "wife" in human:
                if human["wife"] is not None:
                    human["name"].wife = Person.people[human["wife"]]
            elif "husband" in human:
                if human["husband"] is not None:
                    human["name"].husband = Person.people[human["husband"]]
        return [every["name"] for every in people]
        pass
