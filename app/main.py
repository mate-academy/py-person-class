class Person:

    people = {}  # name: Person

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result_list = []

    for person in people:
        temp_person = Person(person["name"], person["age"])
        result_list.append(temp_person)

    for person in people:
        me = Person.people[person["name"]]

        spouse_name = person.get("wife")
        if spouse_name:
            spouse = Person.people[spouse_name]
            me.wife = spouse
            if not hasattr(spouse, "husband"):
                spouse.husband = me

        spouse_name = person.get("husband")
        if spouse_name:
            spouse = Person.people[spouse_name]
            me.husband = spouse
            if not hasattr(spouse, "wife"):
                spouse.wife = me

    return result_list
