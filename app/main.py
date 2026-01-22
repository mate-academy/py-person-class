class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person_dict in people:

        spouse_key = "husband" if person_dict.get("husband") is not None \
            else "wife"
        spouse_name = person_dict.get(spouse_key)

        name = person_dict["name"]

        if spouse_name is not None:
            setattr(Person.people[name],
                    spouse_key,
                    Person.people[spouse_name])

    return person_list
