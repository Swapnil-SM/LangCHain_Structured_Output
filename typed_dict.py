from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'swapnil', 'age':'35'} # here we define age as string instead of int but it not generate1s any error..

print(new_person)