class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    @classmethod
    def get_person(cls, name: str) -> "Person":
        return cls.people.get(name)


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)

        if person.get("wife") is not None and person["wife"] != "":
            wife_name = person["wife"]
            wife = Person.get_person(wife_name)
            if wife:
                new_person.wife = wife
                wife.husband = new_person

        elif person.get("husband") is not None and person["husband"] != "":
            husband_name = person["husband"]
            husband = Person.get_person(husband_name)
            if husband:
                new_person.husband = husband
                husband.wife = new_person

        person_list.append(new_person)
    return person_list
