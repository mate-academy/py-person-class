class Person:
    people = {}

    def __init__(self, name: str, age: int, *spouse) -> None:
        self.name = name
        self.age = age
        self.spouse = spouse
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for pers in people:
        name = pers["name"]
        age = pers["age"]
        spouse_name = pers.get("wife") or pers.get("husband")

        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse is None:
                spouse = Person(spouse_name, None)

            if "wife" in pers:
                person = Person(name, age, spouse)
                person.wife = spouse
                spouse.husband = person
            else:
                person = Person(name, age, spouse)
                person.husband = spouse
                spouse.wife = person
        else:
            person = Person(name, age, None)

        person_list.append(person)

    return person_list
