class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for per in people:
        person = Person(per["name"], per["age"])
        people_list.append(person)
    for per in people:
        name = per["name"]
        spouse_key = "wife" if "wife" in per \
            else "husband"
        spouse_name = per[spouse_key]
        if spouse_name is not None:
            setattr(Person.people[name], spouse_key,
                    Person.people[spouse_name])
    return people_list
