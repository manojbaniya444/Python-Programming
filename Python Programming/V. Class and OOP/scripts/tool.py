"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    
    def gatherAttributes(self):
        attributes = []
        for key in sorted(self.__dict__):
            attributes.append(f"{key}={getattr(self, key)}")
        return ", ".join(attributes)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.gatherAttributes()}"
    
if __name__ == "__main__":
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
            
    class SubTest(TopTest):
        pass
    
    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)