class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    @classmethod
    def couple_create(cls, name: str, couple_name: str, is_male: bool) -> None:
        if couple_name in cls.people and is_male:
            cls.people[name].wife = cls.people[couple_name]
        else:
            cls.people[name].husband = cls.people[couple_name]


def create_person_list(people: list) -> list:
    list_of_people = [Person(person["name"], person["age"])
                      for person in people]
    for person in people:
        if person.get("wife"):
            Person.couple_create(person["name"], person["wife"], True)
        elif person.get("husband"):
            Person.couple_create(person["name"], person["husband"], False)
    return list_of_people
