class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})

    def add_partner(self, partner_type: str, partner_name: str) -> None:
        if partner_name not in self.people.keys():
            return
        if partner_type == "wife":
            self.wife = self.people[partner_name]
        else:
            self.husband = self.people[partner_name]


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = add_basic_info(people)
    add_partner(people)
    return person_list


def add_basic_info(people: list[dict]) -> list[Person]:
    return [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]


def add_partner(people: list[dict]) -> None:
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict:
            person.add_partner("wife", person_dict["wife"])
        if "husband" in person_dict:
            person.add_partner("husband", person_dict["husband"])
