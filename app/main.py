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
        person_name = Person.people[person["name"]]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            if "wife" in person:
                person_name.spouse(spouse_name, "wife")
            else:
                person_name.spouse(spouse_name, "husband")

    return people_list
