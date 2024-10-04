class Person:
    people: {str, "Person"} = {}

    def __init__(self, name: str = None, age: int = None) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list[dict]) -> list:
    person_list = [Person(person.get("name"),
                          person.get("age")) for person in people]
    for num_person in range(len(people)):
        if people[num_person].get("wife"):
            person_list[num_person].wife = Person.people.get(
                people[num_person].get("wife"))
        if people[num_person].get("husband"):
            person_list[num_person].husband = Person.people.get(
                people[num_person].get("husband"))
    return person_list
