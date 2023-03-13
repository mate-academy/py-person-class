class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    people_instances = []

    for person_dict in people:
        people_instances.append(
            Person(person_dict["name"], person_dict["age"])
        )

    for person_dict in people:
        if "wife" in person_dict \
                and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]

            for person_instance in people_instances:
                if person_instance.name == person_dict["name"]:

                    for wife in people_instances:
                        if wife.name == wife_name:
                            person_instance.wife = wife
                            break

        if "husband" in person_dict \
                and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]

            for person_instance in people_instances:
                if person_instance.name == person_dict["name"]:

                    for husband in people_instances:
                        if husband.name == husband_name:
                            person_instance.husband = husband
                            break

        return people_instances
