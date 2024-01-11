class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: list[dict]) -> list:
    person_list = []
    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        spouse_name = person_data.get("wife") or person_data.get("husband")

        person = Person(name, age)

        if spouse_name:
            if spouse_name not in Person.people:
                spouse = Person(spouse_name, None)
                Person.people[spouse_name] = spouse

            spouse = Person.people[spouse_name]
            person.wife = spouse
            spouse.husband = person

        person_list.append(person)

    return person_list
