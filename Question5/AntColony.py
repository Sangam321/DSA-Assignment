import numpy as np
import random

class AntColony:
    def __init__(self, distances, num_ants, num_iterations, decay_factor, alpha, beta):
        self.distances = distances
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay_factor = decay_factor
        self.alpha = alpha
        self.beta = beta
        self.num_cities = len(distances)
        self.pheromone_levels = np.ones((self.num_cities, self.num_cities)) / (self.num_cities * self.num_cities)
        self.best_path = []
        self.best_distance = float('inf')

    def initialize_pheromones(self):
        self.pheromone_levels = np.ones((self.num_cities, self.num_cities)) / (self.num_cities * self.num_cities)

    def solve(self):
        # Main loop for the number of iterations
        for _ in range(self.num_iterations):
            ant_paths = []
            ant_distances = np.zeros(self.num_ants)
            # Construct solutions for each ant
            for ant_index in range(self.num_ants):
                path = self.construct_solution(random.randint(0, self.num_cities - 1))
                ant_paths.append(path)
                ant_distances[ant_index] = self.calculate_distance(path)
                # Update best path if a shorter path is found
                if ant_distances[ant_index] < self.best_distance:
                    self.best_distance = ant_distances[ant_index]
                    self.best_path = list(path)
            self.update_pheromones(ant_paths, ant_distances)
            self.decay_pheromones()

    def construct_solution(self, starting_city):
        # Construct a solution for a single ant
        path = [starting_city]
        visited = [False] * self.num_cities
        visited[starting_city] = True
        while len(path) < self.num_cities:
            current_city = path[-1]
            next_city = self.select_next_city(current_city, visited)
            path.append(next_city)
            visited[next_city] = True
        path.append(starting_city)  # Complete the cycle
        return path

    def select_next_city(self, current_city, visited):
        # Select the next city for an ant based on pheromone levels 
        probabilities = np.zeros(self.num_cities)
        total_probability = 0
        for i in range(self.num_cities):
            if not visited[i]:
                probabilities[i] = (self.pheromone_levels[current_city][i] ** self.alpha) * \
                                   ((1.0 / self.distances[current_city][i]) ** self.beta)
                total_probability += probabilities[i]
        random_value = random.random() * total_probability
        cumulative_probability = 0
        for i in range(self.num_cities):
            if not visited[i]:
                cumulative_probability += probabilities[i]
                if cumulative_probability >= random_value:
                    return i

    def calculate_distance(self, path):
        # Calculate the total distance of a path
        distance = 0
        for i in range(len(path) - 1):
            distance += self.distances[path[i]][path[i + 1]]
        return distance

    def update_pheromones(self, ant_paths, ant_distances):
        # Update pheromone levels based on ant solutions
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    delta_pheromone = 0
                    for k in range(self.num_ants):
                        path = ant_paths[k]
                        distance = ant_distances[k]
                        if i in path and j in path:
                            delta_pheromone += 1 / distance
                    self.pheromone_levels[i][j] += delta_pheromone

    def decay_pheromones(self):
        self.pheromone_levels *= self.decay_factor

    def get_best_path(self):
        # Get the best path found by the ants
        return self.best_path

    def get_best_distance(self):
        return self.best_distance

if __name__ == "__main__":
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    num_ants = 10
    num_iterations = 100
    decay_factor = 0.5
    alpha = 1
    beta = 2

    ant_colony = AntColony(distances, num_ants, num_iterations, decay_factor, alpha, beta)
    ant_colony.solve()

    best_path = ant_colony.get_best_path()
    best_distance = ant_colony.get_best_distance()

    print("Best path:", best_path)
    print("Best distance:", best_distance)
