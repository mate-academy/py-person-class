class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data, person in zip(people, person_list):
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse is not None:
                if "wife" in person_data:
                    person.wife = spouse
                    spouse.husband = person
                else:
                    person.husband = spouse
                    spouse.wife = person

    return person_list
