class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = [Person(person_dict["name"], person_dict["age"])
                        for person_dict in people_list]

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            spouse = Person.people[spouse_name]
            if person_dict.get("wife"):
                person.wife = spouse
                spouse.husband = person
            elif person_dict.get("husband"):
                person.husband = spouse
                spouse.wife = person

    return person_instances
