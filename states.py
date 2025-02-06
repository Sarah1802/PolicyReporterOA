from state import State

class S0(State):
    REMAINDER = 0
    def handle_state(self, context, bit):
        
        if bit == "1":
            context.set_state(S1())
        else:
            context.set_state(S0())

    def get_remainder(self):
        return self.REMAINDER

class S1(State):
    REMAINDER = 1

    def handle_state(self, context, bit):
        
        if bit == "1":
            context.set_state(S0())
        else:
            context.set_state(S2())
    
    def get_remainder(self):
        return self.REMAINDER

class S2(State):
    REMAINDER = 2

    def handle_state(self, context, bit):
        if bit == "0":
            context.set_state(S1())
        else:
            context.set_state(S2())
      
    
    def get_remainder(self):
        return self.REMAINDER