class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    result = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_data
    ]

    for person_data in people_data:
        person_obj = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]

    return result
