class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]
    for person in people:
        wife_name = person.get("wife")
        if wife_name is not None:
            Person.people[person["name"]].wife = Person.people.get(wife_name)
    Person.people[person["name"]].husband = (
        (Person.people)[person["husband"]]
    )
    return result_list
