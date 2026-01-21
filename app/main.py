class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []

    for person_dict in people_list:
        person_instance = Person(person_dict["name"], person_dict["age"])
        person_instances.append(person_instance)

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name and Person.people.get(wife_name):
            person_instance.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person_instance
        if husband_name and Person.people.get(husband_name):
            person_instance.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person_instance

    return person_instances
