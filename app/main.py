class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(raw_people: list[dict]) -> list:
    Person.people.clear()

    _ = [Person(person_data.get("name"), person_data.get("age"))
         for person_data in raw_people]

    for person_data in raw_people:
        person = Person.people[person_data.get("name")]

        wife_name = person_data.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)

        husband_name = person_data.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return [Person.people[person_data.get("name")]
            for person_data in raw_people]
