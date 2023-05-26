class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    def __repr__(self) -> str:
        return f"<Person name={self.name}>"


def create_person_list(people_data: list) -> list[Person]:
    person_list = []
    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name=name, age=age)
        person_list.append(person)

    for person_dict in people_data:
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person = Person.people[person_dict["name"]]
            wife = Person.people[wife_name]
            person.wife = wife
        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person = Person.people[person_dict["name"]]
            person.husband = Person.people[husband_name]
    return person_list
