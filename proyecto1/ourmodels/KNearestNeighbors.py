import numpy as np


class KNearestNeighbors:
    def __init__(self, X_train, y_train, n_neighbors=5, weights="uniform", n_classes=3):
        self.X_train = X_train
        self.y_train = y_train

        self.n_neighbors = n_neighbors
        self.weights = weights

        self.n_classes = n_classes

    def euclidian_distance(self, a, b):
        return np.sqrt(np.sum((a - b) ** 2, axis=1))

    def cosine_distance(self, a, b):
        # Calcula la norma Euclidiana de a y de cada fila de b
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b, axis=1)

        # Calcula el producto punto entre a y cada fila de b
        dot_ab = np.dot(a, b.T)

        # Calcula la cosine similarity entre a y cada fila de b
        cosine_sim = dot_ab / (norm_a * norm_b)

        # Retorna la distancia entre los angulos la cual esta definida como 1 - cosine_similarity
        return 1 - cosine_sim

    def kneighbors(self, X_test, return_distance=False):
        dist = []
        neigh_ind = []

        point_dist = []
        for x_test in X_test:
            point_dist += [self.euclidian_distance(x_test, self.X_train)]

        for row in point_dist:
            enum_neigh = enumerate(row)
            sorted_neigh = sorted(enum_neigh, key=lambda x: x[1])[: self.n_neighbors]

            ind_list = [tup[0] for tup in sorted_neigh]
            dist_list = [tup[1] for tup in sorted_neigh]

            dist.append(dist_list)
            neigh_ind.append(ind_list)

        if return_distance:
            return np.array(dist), np.array(neigh_ind)

        return np.array(neigh_ind)

    def predict(self, X_test):
        if self.weights == "uniform":
            neighbors = self.kneighbors(X_test)
            y_pred = np.array(
                [
                    np.argmax(np.bincount(self.y_train[neighbor]))
                    for neighbor in neighbors
                ]
            )
            return y_pred

        if self.weights == "distance":
            # Calcula las distancias y los índices de los k vecinos más cercanos
            distances, neigh_indexes = self.kneighbors(X_test, return_distance=True)

            # Calcula las ponderaciones inversas de las distancias
            inv_distances = 1 / distances

            # Normaliza las ponderaciones inversas por fila para obtener una media ponderada
            # inversa de las distancias de los k vecinos más cercanos
            mean_inv_dist = inv_distances / np.sum(inv_distances, axis=1)[:, np.newaxis]

            # Inicializa una lista vacía para almacenar las probabilidades
            proba = []

            # Itera sobre cada fila de mean_inv_dist
            for i, row in enumerate(mean_inv_dist):
                # Obtiene las etiquetas de clase de los k vecinos más cercanos para esta fila
                row_pred = self.y_train[neigh_indexes[i]]

                # Itera sobre cada clase y calcula la probabilidad de pertenencia a esa clase
                for k in range(self.n_classes):
                    # Encuentra los índices de los vecinos que pertenecen a la clase k
                    indices = np.where(row_pred == k)
                    # Suma las ponderaciones inversas de los vecinos que pertenecen a la clase k
                    prob_ind = np.sum(row[indices])
                    # Añade la probabilidad de pertenencia a la clase k a la lista de probabilidades
                    proba.append(np.array(prob_ind))

            # Convierte la lista de probabilidades en un arreglo y le da forma de matriz
            predict_proba = np.array(proba).reshape(len(X_test), self.n_classes)

            # Asigna la clase con la probabilidad más alta a cada punto de prueba
            y_pred = np.argmax(predict_proba, axis=1)

            return y_pred

    def score(self, y_test, y_pred):
        return float(sum(y_pred == y_test)) / float(len(y_test))