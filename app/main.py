class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_obj = Person.people[person["name"]]
        if person.get("wife") or person.get("husband"):
            spouse = (person["wife"] if person.get("wife")
                      else person["husband"])
            spouse_info = Person.people.get(spouse)
        if person.get("wife"):
            person_obj.wife = spouse_info
            person_obj.wife.husband = person_obj
        if person.get("husband"):
            person_obj.husband = spouse_info
            person_obj.husband.wife = person_obj
    return person_list
