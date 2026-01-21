class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[self.name] = self

    def __repr__(self) -> str:
        return (f"Person(name={self.name}, age={self.age}, "
                f"wife={self.wife.name if self.wife else None}, "
                f"husband={self.husband.name if self.husband else None})")


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_data:
                    person.wife = spouse
                else:
                    person.husband = spouse

    for person in person_list:
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband

    return person_list
