class Person:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname
  def myprint(self):
    print('my name is ', self.fname, self.lname)
class Me(Person):
  def __init__(self,fname,lname):
    super().__init__(fname,lname)
    self.gender = 'boy'
  def printforme(self):
    print('mu name is', self.fname, self.lname, 'and my love is a', self.gender)
x = Me('khoa','deptrai')
x.printforme()

