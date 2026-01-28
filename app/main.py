class People:
    def __init__(self, person, name, age, gender, spouse):
        self.person = person
        self.name = name
        self.age = age
        self.gender = gender
        self.spouse = spouse
        person = {
        "name": None,
        "age": None,
        "gender": None,
        "spouse": None
        }
class Person:
    people = {}
    def __init__(self,name: str, age: int):
        self.name: str = name
        self.age: int = age        
        Person.people[name] = self
    def create_list_person():
        return [People(name), People(age) for name in names if name:str = name,age:int = age in class Person)
