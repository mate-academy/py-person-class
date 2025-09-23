class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    """
    people_data: список словників з ключами:
    - name: str
    - age: int
    - wife/husband: str або None
    Повертає список об'єктів Person
    """
    person_list = []
    for pdata in people_data:
        person = Person(pdata["name"], pdata["age"])
        person_list.append(person)

    for pdata in people_data:
        person = Person.people[pdata["name"]]
        if "wife" in pdata and pdata["wife"]:
            setattr(person, "wife", Person.people[pdata["wife"]])
        if "husband" in pdata and pdata["husband"]:
            setattr(person, "husband", Person.people[pdata["husband"]])

    return person_list
