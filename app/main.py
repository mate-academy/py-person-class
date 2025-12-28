class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    [Person(person_dict["name"], person_dict["age"])
     for person_dict in people_data]

    person_list = []
    for person_dict in people_data:
        name = person_dict["name"]
        person = Person.people[name]

        person_list.append(person)

        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]

        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]

    return person_list
