class Weights:
    def __init__(self, unique_weights, weights, amount):
        self.all_weights = []
        self.unique_weights = unique_weights
        self.weights = weights
        self.amount = amount

    def create_weight_array(self):
        for i, w in enumerate(self.weights):
            self.all_weights.extend([self.weights[i]] * self.amount[i])
        return self.all_weights
