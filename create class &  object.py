class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Data:
  def __init__(self, add , pin):
      self.add = add
      self.pin = pin

def main():
    p1 = Person("John", 36)
    p2 = Data("Sus-Pune", 411021)
    print(p1.name)
    print(p1.age)
    print(p2.add)
    print(p2.pin)
if __name__=="__main__":
    main()