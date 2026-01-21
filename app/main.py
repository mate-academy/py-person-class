class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    users_list = [Person(data["name"], data["age"]) for data in people_data]

    for data in people_data:
        name = data["name"]
        person = Person.people[name]

        wife_name = data.get("wife")
        if wife_name is not None:
            person.wife = Person.people.get(wife_name)

        husband_name = data.get("husband")
        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return users_list
