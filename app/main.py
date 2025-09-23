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
    Повертає список обєктів Person
    """
    person_list = [Person(pdata["name"], pdata["age"])for pdata in people_data]

    for pdata in people_data:
        person = Person.people[pdata["name"]]
        wife_name = pdata.get("wife")
        husband_name = pdata.get("husband")
        if wife_name:
            setattr(person, "wife", Person.people[wife_name])
        if husband_name:
            setattr(person, "husband", Person.people[husband_name])

    return person_list
