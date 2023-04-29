import math
import numpy as np


def entropy_func(c, n):
    return -(c * 1.0 / n) * math.log(c * 1.0 / n, 2)


def entropy_cal(c1, c2):
    # entropy between class 1 and 2
    if c1 == 0 or c2 == 0:  # when there is only one class in the group, entropy is 0
        return 0
    return entropy_func(c1, c1 + c2) + entropy_func(c2, c1 + c2)


# One versus All
# c1,c2,c3, .., cm
# c1, *
# c2, *
# c3, *
# ...
# cm, *


# each class versus the others
def entropy_of_one_division(division):
    s = 0
    n = len(division)
    classes = set(division)
    for c in classes:  # for each class, get entropy
        n_c = sum(division == c)
        e = (
            n_c * 1.0 / n * entropy_cal(sum(division == c), sum(division != c))
        )  # weighted avg
        s += e
    return s, n


# The whole entropy
def get_entropy(y_predict, y_real):
    if len(y_predict) != len(y_real):
        print("They have to be the same length")
        return None
    n = len(y_real)
    s_true, n_true = entropy_of_one_division(
        y_real[y_predict]
    )  # left hand side entropy
    s_false, n_false = entropy_of_one_division(
        y_real[~y_predict]
    )  # right hand side entropy
    s = (
        n_true * 1.0 / n * s_true + n_false * 1.0 / n * s_false
    )  # overall entropy, again weighted average
    return s


class DecisionTreeClassifier(object):
    def __init__(self, max_depth):
        self.depth = 0
        self.max_depth = max_depth

    def fit(self, feature_names, x, y, par_node={}, depth=0):
        if par_node is None:
            return None
        elif len(y) == 0:
            return None
        elif self.all_same(y):
            return {"val": y[0]}
        elif depth >= self.max_depth:
            return None
        else:
            col, cutoff, entropy = self.find_best_split_of_all(
                x, y
            )  # find one split given an information gain
            y_left = y[x[:, col] < cutoff]
            y_right = y[x[:, col] >= cutoff]
            par_node = {
                "col": feature_names[col],
                "index_col": col,
                "cutoff": cutoff,
                "val": np.round(np.mean(y)),
            }
            par_node["left"] = self.fit(x[x[:, col] < cutoff], y_left, {}, depth + 1)
            par_node["right"] = self.fit(x[x[:, col] >= cutoff], y_right, {}, depth + 1)
            self.depth += 1
            self.trees = par_node
            return par_node

    # all features versus values, get best
    def find_best_split_of_all(self, x, y):
        # print(x.shape, y.shape)
        col = None
        min_entropy = 1
        cutoff = None
        for i, c in enumerate(x.T):
            entropy, cur_cutoff = self.find_best_split(c, y)
            if entropy == 0:  # find the first perfect cutoff. Stop Iterating
                return i, cur_cutoff, entropy
            elif entropy <= min_entropy:
                min_entropy = entropy
                col = i
                cutoff = cur_cutoff
        return col, cutoff, min_entropy

    # one feature versus values
    def find_best_split(self, col, y):
        min_entropy = 10
        n = len(y)
        for value in set(col):
            y_predict = col < value  # get which ones are less than
            my_entropy = get_entropy(y_predict, y)
            if my_entropy <= min_entropy:
                min_entropy = my_entropy
                cutoff = value
        return min_entropy, cutoff

    def all_same(self, items):
        return all(x == items[0] for x in items)

    def predict(self, x):
        tree = self.trees
        results = np.array([0] * len(x))
        for i, c in enumerate(x):
            results[i] = self._get_prediction(c)
        return results

    def _get_prediction(self, row):
        cur_layer = self.trees
        cur_layer_parent = None
        while cur_layer.get('cutoff'):
            cur_layer_parent = cur_layer
            if row[cur_layer['index_col']] < cur_layer['cutoff']:
                cur_layer = cur_layer['left']
            else:
                cur_layer = cur_layer['right']
            if cur_layer is None:
                return np.round(cur_layer_parent['val'])
        return cur_layer.get('val')