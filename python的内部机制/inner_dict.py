class Test:
    def __init__(self, name):
        self.name = name


print(Test.__dict__)
test = Test('jeff')
print(test.__dict__)
print(dir(Test))
print(dir(test))

test.__dict__['hack'] = 'hack'
# Test.__dict__['Hack'] = 'Hack'
setattr(Test, 'Hack', 'Hack')
Test.Hack = 'Hack'
print(test.hack)
print(Test.Hack)
