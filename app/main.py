class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    @classmethod
    def add_wife(cls, people: list) -> None:
        for person in people:
            wife = person.get("wife")
            if wife:
                cls.people[person.get("name")].wife = Person.people[wife]

    @classmethod
    def add_husband(cls, people: list) -> None:
        for person in people:
            husband = person.get("husband")
            if husband:
                cls.people[person.get("name")].husband = Person.people[husband]


def create_person_list(people: list) -> list:
    list_person = []
    for person in people:
        person_instance = Person(person["name"], person["age"])
        list_person.append(person_instance)

    Person.add_wife(people)
    Person.add_husband(people)
    return list_person
