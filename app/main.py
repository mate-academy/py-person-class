class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    list_of_people = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for i in range(len(people)):
        if Person.people.get(people[i].get("wife")) is not None:
            list_of_people[i].wife = Person.people.get(people[i].get("wife"))
        elif Person.people.get(people[i].get("husband")) is not None:
            list_of_people[i].husband = (
                Person.people.get(people[i].get("husband")))

    return list_of_people
