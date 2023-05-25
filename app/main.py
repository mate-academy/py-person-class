class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    def __repr__(self) -> str:
        return f"<Person name={self.name}>"


def create_person_list(people_data: list) -> list:
    person_list = []
    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name=name, age=age)
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person
        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person
        person_list.append(person)
    return person_list
