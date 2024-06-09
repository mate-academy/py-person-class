class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: dict) -> list:
    for single_person in people:
        Person(single_person["name"], single_person["age"])

    for single_person in people:
        person = Person.people[single_person["name"]]
        spouse_name = single_person.get("wife") or single_person.get("husband")
        if spouse_name:
            spouse = Person.people[spouse_name]
            if "wife" in single_person:
                person.wife = spouse
            else:
                person.husband = spouse
            person.spouse = spouse

    return list(Person.people.values())
