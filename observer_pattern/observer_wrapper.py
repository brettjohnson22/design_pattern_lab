from publisher import Publisher
from subscriber import Subscriber


''' Obvserver Design Pattern '''
print('\nObserver Design Pattern\n')
publisher = Publisher()

mike = Subscriber('Mike')
nevin = Subscriber('Nevin')
jj = Subscriber('JJ')

publisher.register(mike)
publisher.register(nevin)
publisher.register(jj)

publisher.dispatch('Python Rocks!')
publisher.unregister(nevin)
publisher.dispatch('Keep working on your design patterns!')