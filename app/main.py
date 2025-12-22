class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for i in range(len(people)):
        if people[i].get("wife") is not None:
            list_of_people[i].wife = people[i].get("wife")
        elif people[i].get("husband") is not None:
            list_of_people[i].husband = people[i].get("husband")

    for person in list_of_people:
        if (hasattr(person, "wife")
                and Person.people.get(person.wife) is not None):
            person.wife = Person.people[person.wife]
        if (hasattr(person, "husband")
                and Person.people.get(person.husband) is not None):
            person.husband = Person.people[person.husband]

    return list_of_people
