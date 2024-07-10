class PrimeFactors:
    def __init__(self):
        self.param = 1
        self.result = []

    def of(self, param):
        self.param = param
        if param == 1:
            return []
        self.recursive_process(2)
        return self.result

    def recursive_process(self, n):
        if self.param == 1:
            return
        if self.param % n == 0:
            self.param = self.param // n
            self.result.append(n)
            self.recursive_process(2)
        else:
            self.recursive_process(n+1)