class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    temp_list = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }

    for person in people:
        person_obj = temp_list[person["name"]]
        if temp_list.get(person.get("wife")):
            person_obj.wife = temp_list[person["wife"]]
        if temp_list.get(person.get("husband")):
            person_obj.husband = temp_list[person["husband"]]
        Person.people[person_obj.name] = person_obj
    return list(temp_list.values())
