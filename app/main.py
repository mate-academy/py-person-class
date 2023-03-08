class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict[str, any]]) -> list[Person]:
    list_of_person = [
        Person(persona["name"],
               persona["age"])
        for persona in people
    ]
    for persona in people:
        for key in persona:
            if key == "wife" and persona["wife"] is not None:
                Person.people[
                    persona
                    ["name"]].wife = Person.people[persona["wife"]]
            elif key == "husband" and persona["husband"] is not None:
                Person.people[
                    persona
                    ["name"]].husband = Person.people[persona["husband"]]
    return list_of_person
