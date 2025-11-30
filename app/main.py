class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(people_data["name"], people_data["age"])
                   for people_data in people]

    for people_data in people:
        person = Person.people[people_data["name"]]

        wife_name = people_data.get("wife")
        wife_obj = Person.people.get(wife_name)
        if wife_name and wife_obj:
            person.wife = wife_obj
            wife_obj.husband = person

        husband_name = people_data.get("husband")
        husband_obj = Person.people.get(husband_name)
        if husband_name and husband_obj:
            person.husband = husband_obj
            husband_obj.wife = person
    return people_list
