class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in person_list:
        person_key = next(person_in_list for person_in_list in people
                          if person_in_list["name"] == person.name)
        if person_key.get("wife") or person_key.get("husband"):
            spouse = (person_key["wife"] if person_key.get("wife")
                      else person_key["husband"])
            spouse_info = person.people.get(spouse)
            if person_key.get("wife"):
                person.wife = spouse_info
                person.wife.husband = person
            else:
                person.husband = spouse_info
                person.husband.wife = person
    return person_list
