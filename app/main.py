class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_links = []
    new_person = None
    list_result = []

    for member in people:
        list_links.append(Person(member["name"], member["age"]))

    for member in people:
        if "wife" in member and member["wife"]:
            new_person = Person.people.get(member["name"])
            new_person.wife = Person.people.get(member["wife"])
            list_result.append(new_person)

        elif "husband" in member and member["husband"]:
            new_person = Person.people.get(member["name"])
            new_person.husband = Person.people.get(member["husband"])
            list_result.append(new_person)

        else:
            new_person = Person.people.get(member["name"])
            list_result.append(new_person)

    return list_result
