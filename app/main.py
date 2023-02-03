class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list[Person]:
    result = []
    for person in people:
        result.append(Person(person.get("name"), person.get("age")))

    for person_for_engagement in people:
        if person_for_engagement.get("wife"):
            Person.people[
                person_for_engagement.get("name")
            ].wife = Person.people[person_for_engagement.get("wife")]
        if person_for_engagement.get("husband"):
            Person.people[
                person_for_engagement.get("name")
            ].husband = Person.people[person_for_engagement.get("husband")]
    return result
