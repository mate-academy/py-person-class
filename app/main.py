class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        instance = Person.people[person.get("name")]
        if (person.get("wife")
                and Person.people.get(person.get("wife"))):
            instance.wife = Person.people.get(person.get("wife"))
        elif (person.get("husband")
              and Person.people.get(person.get("husband"))):
            instance.husband = Person.people.get(person.get("husband"))
    return instances
