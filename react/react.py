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
        for dep in self.dependents:
            dep.check_for_callbacks()
    

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.function = compute_function
        self.dependents = set()
        self.callbacks = set()
        self.prev_value = self.value = None
        for inp in inputs:
            inp.dependents.add(self)
        self.compute()
        self.check_for_callbacks()

    def compute(self):
        self.value = self.function([inp.value for inp in self.inputs])
        for dep in self.dependents:
            dep.compute()
        
    def check_for_callbacks(self):
        if self.value != self.prev_value:
            self.prev_value = self.value
            self.run_callbacks()
            for dep in self.dependents:
                dep.check_for_callbacks()

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)

    def run_callbacks(self):
        for cb in self.callbacks:
            cb(self.value)
