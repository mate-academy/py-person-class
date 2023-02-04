class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    @classmethod
    def add_partner(cls, people: list) -> None:
        for person in people:
            wife = person.get("wife")
            husband = person.get("husband")
            if wife:
                cls.people[person.get("name")].wife = cls.people[wife]
            if husband:
                cls.people[person.get("name")].husband = cls.people[husband]


def create_person_list(people: list) -> list:
    list_person = []
    for person in people:
        person_instance = Person(person["name"], person["age"])
        list_person.append(person_instance)

    Person.add_partner(people)
    return list_person
