class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def __repr__(self) -> str:
        return f'Person(name="{self.name}", age={self.age})'


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)

        person_list.append(person)

        if "wife" in person_dict and person_dict["wife"]:
            wife_name = person_dict["wife"]
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person

        if "husband" in person_dict and person_dict["husband"]:
            husband_name = person_dict["husband"]
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person

    return person_list
