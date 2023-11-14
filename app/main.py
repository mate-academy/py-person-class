class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(person["name"], person["age"]) for person in people]

    for person_instance, person_data in zip(person_instances, people):
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            wife_or_husband = "wife" if "wife" in person_data else "husband"
            setattr(person_instance, wife_or_husband, spouse_instance)

    return person_instances
