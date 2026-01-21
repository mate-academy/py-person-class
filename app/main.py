class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list:
    # create new list with objects
    new_list = [Person(people[i]["name"], people[i]["age"])
                for i in range(len(people))]
    for obj in range(len(new_list)):
        if people[obj].get("wife"):
            new_list[obj].wife = Person.people[people[obj].get("wife")]

        if people[obj].get("husband"):
            new_list[obj].husband = Person.people[people[obj].get("husband")]
    return new_list
