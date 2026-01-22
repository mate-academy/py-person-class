class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person_instance.get("name"),
                     person_instance.get("age"))
              for person_instance in people]

    for person_instance in people:
        name = person_instance["name"]
        if person_instance.get("wife"):
            Person.people[name].wife = (
                Person.people)[person_instance.get("wife")]
        elif person_instance.get("husband"):
            Person.people[name].husband = (
                Person.people)[person_instance.get("husband")]
    return result
