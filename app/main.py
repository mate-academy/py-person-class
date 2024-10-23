class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list) -> list:
    person_instances = []

    for person in people_list:
        person_instance = Person(person["name"], person["age"])
        person_instances.append(person_instance)

    for person in people_list:
        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            if wife_name in Person.people:
                Person.people[person["name"]].wife = Person.people[wife_name]
            else:
                print(f"Warning: Wife {wife_name} not found for {person["name"]}")
        elif "husband" in person and person["husband"]:
            husband_name = person["husband"]
            if husband_name in Person.people:
                Person.people[person["name"]].husband = Person.people[husband_name]
            else:
                print(f"Warning: Husband {husband_name} not found for {person["name"]}")

    return person_instances
