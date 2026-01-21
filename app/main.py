class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def add_partner(cls, people: list) -> None:
        for person in people:
            person_wife = person.get("wife")
            person_husband = person.get("husband")
            person_name = person.get("name")
            if person_wife:
                cls.people[person_name].wife = cls.people[person_wife]
            if person_husband:
                cls.people[person_name].husband = cls.people[person_husband]


def create_person_list(people: list) -> list:
    list_person = []
    for person in people:
        person_instance = Person(person["name"], person["age"])
        list_person.append(person_instance)

    Person.add_partner(people)
    return list_person
