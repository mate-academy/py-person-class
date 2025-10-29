class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_instances = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person_data in people:
        name = person_data["name"]
        instance = Person.people[name]

        relationship_key = None
        spouse_name = None

        if person_data.get("wife"):
            relationship_key = "wife"
            spouse_name = person_data["wife"]

        elif person_data.get("husband"):
            relationship_key = "husband"
            spouse_name = person_data["husband"]

        if spouse_name and relationship_key:
            spouse_instance = Person.people.get(spouse_name)

            if spouse_instance:
                setattr(instance, relationship_key, spouse_instance)

    return person_instances
