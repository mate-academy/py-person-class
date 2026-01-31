class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"<Object Person, {self.__dict__}>"


def create_person_list(people: list) -> list:
    Person.people.clear()
    result_list = [
        Person(
            name=person.get("name"),
            age=person.get("age"))
        for person in people]

    for person in people:

        person_name = person.get("name")
        person_object = Person.people.get(person_name)

        if person.get("wife") in Person.people.keys():
            wife_name = person.get("wife")
            wife = Person.people.get(wife_name)
            person_object.wife = wife
        elif person.get("husband") in Person.people.keys():
            husband_name = person.get("husband")
            husband = Person.people.get(husband_name)
            person_object.husband = husband

    return result_list
