class Person:
    people: dict = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.add_people(self)

    @classmethod
    def add_people(cls, person) -> None:
        cls.people[person.name] = person

    def __repr__(self,):
        return f"<Person = name : {self.name}, age : {self.age}>"


def create_person_list(people: list) -> list:
    person_list = []
    for i in people:
        person = Person(i.get("name"), i.get("age"))
        person_list.append(person)

    for j in people:
        name = j.get("name", "")
        wife, husband = j.get("wife", None), j.get("husband", None)
        person = list(filter(lambda x: x.name == name, person_list))[0]
        if wife:
            partner = list(filter(lambda x: x.name == wife, person_list))[0]
            person.wife = partner
        if husband:
            partner = list(filter(lambda x: x.name == husband, person_list))[0]
            person.husband = partner

    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
