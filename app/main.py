class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(name=person_data["name"], age=person_data["age"])
                   for person_data in people]

    for person_data in people:
        person = Person.people[person_data["name"]]
        spouse_key = "wife" if "wife" in person_data else "husband"
        spouse_name = person_data.get(spouse_key)
        if spouse_name:
            setattr(person, spouse_key, Person.people[spouse_name])

    return person_list
