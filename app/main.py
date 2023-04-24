class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


def create_person_list(people: list) -> list:
    list_instances = []
    for person_dict in people:
        person_instance = Person(person_dict["name"], person_dict["age"])

        if person_dict.get("wife"):
            wife = Person.people.get(person_dict.get("wife"))

            if wife:
                person_instance.wife = wife
                wife.husband = person_instance
        elif person_dict.get("husband"):
            husband = Person.people.get(person_dict.get("husband"))

            if husband:
                person_instance.husband = husband
                husband.wife = person_instance
        list_instances.append(person_instance)
    return list_instances
