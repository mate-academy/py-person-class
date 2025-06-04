class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:

    [Person(person_dict["name"], person_dict["age"])
     for person_dict in people_data]

    for person_dict in people_data:
        person_instance = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person_instance.wife = Person.people.get(wife_name)
        if husband_name:
            person_instance.husband = Person.people.get(husband_name)

    return list(Person.people.values())
