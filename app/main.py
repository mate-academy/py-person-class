
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    @classmethod
    def create_instances(cls, list_of_people: list[dict]) -> None:
        for person in list_of_people:
            cls(person["name"], person["age"])

    @classmethod
    def check_for_pair(cls, list_of_people: list[dict]) -> None:
        for person_info in list_of_people:
            current_person = cls.people[person_info["name"]]
            if person_info.get("wife") is not None:
                current_person.wife = cls.people[person_info["wife"]]
                cls.people[person_info["wife"]].husband = current_person


def create_person_list(list_of_people: list[dict]) -> list:
    Person.create_instances(list_of_people)
    Person.check_for_pair(list_of_people)
    list_of_persons = [person for person in Person.people.values()]
    return list_of_persons
