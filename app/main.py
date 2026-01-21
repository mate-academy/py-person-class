class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    output_list = [Person(name=person["name"],
                          age=person["age"]) for person in people]
    for person in people:
        name = person["name"]
        obj = Person.people[name]
        wife_name = person.get("wife")
        if wife_name:
            obj.wife = Person.people[wife_name]
        husband_name = person.get("husband")
        if person.get("husband"):
            obj.husband = Person.people[husband_name]
    return output_list
