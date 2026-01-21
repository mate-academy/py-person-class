class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_list = [
        Person(person.get("name"), person.get("age")) for person in people_list
    ]
    for i in range(len(people_list)):
        if people_list[i].get("wife") or people_list[i].get("husband"):
            for index in range(len(people_list)):
                if people_list[i].get("wife") == person_list[index].name:
                    person_list[i].wife = person_list[index]
                    break
                elif people_list[i].get("husband") == person_list[index].name:
                    person_list[i].husband = person_list[index]
                    break

    return person_list
