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

        if wife_name:
            wife_instance = Person.people.get(wife_name)
            if wife_instance:
                person_instance.wife = wife_instance
                wife_instance.husband = person_instance

        if husband_name:
            husband_instance = Person.people.get(husband_name)
            if husband_instance:
                person_instance.husband = husband_instance
                husband_instance.wife = person_instance

    return person_instances
