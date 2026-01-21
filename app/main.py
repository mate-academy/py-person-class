class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse, role):
        setattr(self, role, spouse)


def create_person_list(people: list) -> list:
    if not people:
        return []

    person_instances = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        person_instance = Person.people[person["name"]]
        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person.get(spouse_key)

        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            if spouse_instance:
                person_instance.set_spouse(spouse_instance, spouse_key)
                spouse_instance.set_spouse(person_instance, "husband" if spouse_key == "wife" else "wife")

    return person_instances
