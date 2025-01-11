class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if "wife" in person:
                person_instance.wife = spouse
            elif "husband" in person:
                person_instance.husband = spouse
    return person_list
