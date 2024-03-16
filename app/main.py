class Person:
    people = {}

    def __init__(self, name: str = "", age: int = 0) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(people[i]["name"], people[i]["age"])
                for i in range(len(people))]
    for obj in range(len(new_list)):
        if "wife" in people[obj] and people[obj].get("wife") is not None:
            new_list[obj].wife = Person.people[people[obj].get("wife")]

        if "husband" in people[obj] and people[obj].get("husband") is not None:
            new_list[obj].husband = Person.people[people[obj].get("husband")]
    return new_list
