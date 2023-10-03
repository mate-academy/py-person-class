class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list: [Person] = []

    for person in people:
        person_list.append(
            Person(
                name=person["name"],
                age=person["age"]
            )
        )

    # Adding husband and wife for people
    for person in people:
        if person.get("husband") is not None:
            person_obj = Person.people[person["name"]]
            husband_obj = Person.people[person["husband"]]
            person_obj.husband = husband_obj

        if person.get("wife") is not None:
            person_obj = Person.people[person["name"]]
            wife_obj = Person.people[person["wife"]]
            person_obj.wife = wife_obj

    return person_list
