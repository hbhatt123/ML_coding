# Online Python-3 Compiler (Interpreter)
class knn_classifier():
    def __init__(self, distance_metric):
        self.distance_metric = distance_metric
        
    def get_distance_metric(self,training_data_point,test_data_point):
        if self.distance_metric == 'euclidean':
            
            dist = 0
            for i in range(len(training_data_point)-1):
                dist += (training_data_point[i] - test_data_point[i])**2
            euclidean_distance = np.sqrt(dist)
            return euclidean_distance    
        elif self.distance_metric == 'manhattan':
            dist = 0
            for i in range(len(training_data_point)-1):
                dist += abs(training_data_point[i] - test_data_point[i])
            manhattan_distance = dist
            return manhattan_distance
        
        
    def nearest_neighbors(self, x_train, test_data, k):
        dist_list = []
        
        for training_data in x_train:
            distance = self.get_distance_metric(training_data_point,test_data_point)
            dist_list.append(training_data_point,distance)
            
        dist_list.sort(key = lambda x: x[1])     # sort dist_list based on distance (1) not training data (0)
            
            neighbors = []
            for j in range(k):
                neighbors.append(dist_list[j][0])
            return neighbors    
        
    def predict(self,x_train, test_data,k):
        neighbors = self.nearest_neighbors(x_train,test_data,k)
        for data in neighbors:
            label = []
            label.append(data[-1]) # lable form  target column(last one)
            
        predicted_class = statistics.mode(lable) # most repeated value majority class 
        return predicted_class
        
   




if __name__ == '__main__':
    A = [[1,1,2],[2,1,1]]
    B = [[1,2,3],[2,3,1],[1,1,1]]
    
    ans = matrix_mult(A,B)
    print(ans)
