class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(name=item["name"], age=item["age"]) for item in people]
    for person in people:
        if person.get("wife") is not None:
            Person.people.get(person["name"]).wife = (
                Person.people.get(person["wife"])
            )
        if person.get("husband") is not None:
            Person.people.get(person["name"]).husband = (
                Person.people.get(person["husband"])
            )
    return result
