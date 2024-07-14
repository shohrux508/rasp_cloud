class A:
    counter = 0
    def meth(self):
        return 'method'
a = A()
a.counter = 100
print('Equals' if a.counter == A.counter else 'Not equals')
print('Equals' if a.meth() == A.meth(a) else 'Not Equals')
