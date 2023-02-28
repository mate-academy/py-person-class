class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

        
def create_person_list(people: list) -> list:
    list_of_person = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        if "wife" in human and human.get("wife") is not None:
            Person.people[human["name"]].wife = (
                    Person.people[human["wife"]]
            )
        elif "husband" in human and human.get("husband") is not None:
            Person.people[human["name"]].husband = (
                    Person.people[human["husband"]]
            )
    return list_of_person
