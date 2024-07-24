class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        Person(name, age)

    for person_dict in people:
        name = person_dict["name"]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")

        if spouse_name:
            person = Person.people[name]
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_dict:
                    person.wife = spouse
                elif "husband" in person_dict:
                    person.husband = spouse

    return list(Person.people.values())
