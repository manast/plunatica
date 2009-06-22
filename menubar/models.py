


class MenuItem:
    def __init__(self, name, view):
        self.name = name #MenuName (name)
        self.view = view #MenuView (view)
        
    def __unicode__(self):
        return self.name.__unicode__() + "->" + self.view.__unicode__()
            
        

