class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        list_of_people.append(person)
    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]
        spouse = person_data.get("wife") or person_data.get("husband")
        if spouse:
            spouse = Person.people[spouse]
            if "wife" in person_data:
                person.wife = spouse
            else:
                person.husband = spouse
    return list_of_people
