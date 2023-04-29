import numpy as np

class DecisionNode:
    def __init__(self, column=None, value=None, true_branch=None, false_branch=None, result=None):
        self.column = column
        self.value = value
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.result = result

class DecisionTreeClassifier:
    def __init__(self, min_samples=2, max_depth=5):
        self.min_samples = min_samples
        self.max_depth = max_depth
        
    def fit(self, X, y):
        self.n_classes = len(set(y))
        self.n_features = X.shape[1]
        self.tree = self.build_tree(X, y)
        
    def predict(self, X):
        return [self.classify_sample(x, self.tree) for x in X]
    
    def build_tree(self, X, y, max_depth=0):
        num_samples = len(y)
        num_features = X.shape[1]
        num_classes = len(set(y))
        
        if (num_samples < self.min_samples or max_depth == self.max_depth or num_classes == 1):
            return DecisionNode(result=self.calculate_result(y))
        
        best_column, best_value = self.find_best_split(X, y, num_samples, num_features)
        true_indices, false_indices = self.split_data(X[:, best_column], best_value)
        
        true_branch = self.build_tree(X[true_indices,:], y[true_indices], max_depth+1)
        false_branch = self.build_tree(X[false_indices,:], y[false_indices], max_depth+1)
        
        return DecisionNode(best_column, best_value, true_branch, false_branch)
    
    def find_best_split(self, X, y, num_muestras, num_features):
        best_gain = -1
        best_column = None
        best_value = None
        
        for column in range(num_features):
            values = set(X[:,column])
            
            for value in values:
                true_indices, false_indices = self.split_data(X[:,column], value)
                
                if len(true_indices) == 0 or len(false_indices) == 0:
                    continue
                
                gain = self.calculate_gain(y, true_indices, false_indices)
                
                if gain > best_gain:
                    best_gain = gain
                    best_column = column
                    best_value = value
                    
        return best_column, best_value
    
    def split_data(self, feature, value):
        true_indices = np.argwhere(feature <= value).flatten()
        false_indices = np.argwhere(feature > value).flatten()
        
        return true_indices, false_indices
    
    def calculate_gain(self, y, true_indices, false_indices):
        initial_entropy = self.calculate_entropy(y)
        weight_true = len(true_indices) / len(y)
        weight_false = len(false_indices) / len(y)
        entropy_true = self.calculate_entropy(y[true_indices])
        entropy_false = self.calculate_entropy(y[false_indices])
        
        gain = initial_entropy - weight_true * entropy_true - weight_false * entropy_false
        
        return gain
    
    def calculate_entropy(self, y):
        class_distribution = np.array([np.sum(y == c) for c in range(self.n_classes)])
        class_distribution = class_distribution / len(y)
        
        entropy = -np.sum(class_distribution * np.log2(class_distribution + 1e-6))
        
        return entropy

    def calculate_result(self, y):
        class_distribution = np.array([np.sum(y == c) for c in range(self.n_classes)])
        result = np.argmax(class_distribution)
        
        return result

    def classify_sample(self, x, current_node):
        if current_node.result is not None:
            return current_node.result
        
        if x[current_node.column] <= current_node.value:
            return self.classify_sample(x, current_node.true_branch)
        else:
            return self.classify_sample(x, current_node.false_branch)