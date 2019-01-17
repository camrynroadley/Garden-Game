#TrapBag currently holds a basic trap can add other trap types as necessary.


class TrapBag:
    def __init__(self):
        self.num_of_traps = 5
        
    def can_set_trap(self):
        if(self.num_of_traps > 0):
            return True
        else:
            return False
        
    def set_trap(self):
        self.num_of_traps -= 1
