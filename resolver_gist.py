from utemplate.source import Compiler
from uio import StringIO

class Resolver():
    def __init__(self, lookup):
        self.lookup = lookup
    
    def file_open(self, name):
        return StringIO(self.lookup[name])
    


if __name__ == "__main__":
    r = Resolver(dict(
        greeting = "Hello",
        planet =   "World",
        template = "{% include 'greeting' %} {% include 'planet' %}"
    ))

o = StringIO()
c = Compiler(r.file_open('template'), o, loader=r)
c.compile()

print(o.getvalue())