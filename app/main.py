class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.set_person(self)

    @classmethod
    def set_person(cls, other: object) -> None:
        cls.people[other.name] = other

    @classmethod
    def get_person(cls, name: str) -> object:
        return cls.people[name]

    def set_bedfellow(self, bedfellow: str, name: str) -> None:
        if bedfellow == "wife":
            self.wife = self.get_person(name)
        elif bedfellow == "husband":
            self.husband = self.get_person(name)


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person_list.append(Person(human["name"], human["age"]))
    for index in range(len(person_list)):
        if people[index].get("wife", None) is not None:
            person_list[index].set_bedfellow(
                "wife", people[index].get("wife"))
        if people[index].get("husband", None) is not None:
            person_list[index].set_bedfellow(
                "husband", people[index].get("husband"))
    return person_list
