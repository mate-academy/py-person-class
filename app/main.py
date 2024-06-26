class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def spouse(self, spouse_name: str, spouse_type: str) -> None:
        spouse = Person.people.get(spouse_name)
        if spouse_type == "wife":
            self.wife = spouse
            spouse.husband = self
        else:
            self.husband = spouse
            spouse.wife = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = (
                Person.people[person["wife"]]
            )
        elif person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]]
            )

    return people_list
