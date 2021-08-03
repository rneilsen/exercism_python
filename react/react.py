class InputCell:
    def __init__(self, initial_value):
        self.dependents = set()
        self.value = initial_value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        for dep in self.dependents:
            dep.compute()
    

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.function = compute_function
        self.dependents = set()
        for inp in inputs:
            inp.dependents.add(self)
        self.compute()

    def compute(self):
        self.value = self.function([inp.value for inp in self.inputs])
        for dep in self.dependents:
            dep.compute()

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
