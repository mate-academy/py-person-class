class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:

    list_with_instances = []

    for person in people_list:
        list_with_instances.append(
            Person(
                name=person["name"],
                age=person["age"]
            )
        )

    for person in people_list:
        if "wife" in person and person["wife"]:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        elif "husband" in person and person["husband"]:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return list_with_instances
