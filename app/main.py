class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    instance_dict = {}

    for person in people:

        new_instance = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            setattr(new_instance, "wife", person["wife"])

        if "husband" in person and person["husband"] is not None:
            setattr(new_instance, "husband", person["husband"])

        instance_dict[person["name"]] = new_instance
        persons_list.append(new_instance)

    for instance in persons_list:
        if hasattr(instance, "wife"):
            instance.wife = instance_dict.get(instance.wife)

        if hasattr(instance, "husband"):
            instance.husband = instance_dict.get(instance.husband)

    return persons_list
