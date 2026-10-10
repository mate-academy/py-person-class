class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def get_spouse(person: Person, person_dict: dict) -> Person:
    if (person_dict.get("wife")
            and Person.people.get(person_dict["wife"])):
        person.wife = Person.people[person_dict["wife"]]
        Person.people[person_dict["wife"]].husband = person
    if (person_dict.get("husband")
            and Person.people.get(person_dict["husband"])):
        person.husband = Person.people[person_dict["husband"]]
        Person.people[person_dict["husband"]].wife = person
    return person


def create_person_list(people: list) -> list:
    person_list = [get_spouse(Person(person["name"], person["age"]), person)
                   for person in people]
    return person_list
