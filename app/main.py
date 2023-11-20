class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person in people:
        person_list = Person(person["name"], person["age"])
        person_instances.append(person_list)

    for person in people:
        person_list = Person.people[person["name"]]
        right_name = person.get("wife") or person.get("husband")

        if right_name is not None:
            if right_name in Person.people:
                spouse_instance = Person.people[right_name]
                if "wife" in person:
                    person_list.wife = spouse_instance
                    spouse_instance.husband = person_list
                elif "husband" in person:
                    person_list.husband = spouse_instance
                    spouse_instance.wife = person_list

    return person_instances
