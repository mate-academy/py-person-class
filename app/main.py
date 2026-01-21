class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:

    if [len(people) != 0]:
        person_instances = [Person(person["name"], person["age"])
                            for person in people]

        for person in people:
            person_instance = Person.people[person["name"]]

            if "wife" in person and person["wife"] is not None:
                wife_name = person["wife"]
                if wife_name in Person.people:
                    person_instance.wife = Person.people[wife_name]
                else:
                    print(f"Warning: {wife_name} not in Person.people.")
            elif "husband" in person and person["husband"] is not None:
                husband_name = person["husband"]
                if husband_name in Person.people:
                    person_instance.husband = Person.people[husband_name]
                else:
                    print(f"Warning: {husband_name} not in Person.people.")

        return person_instances
