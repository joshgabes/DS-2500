# LAB EXERCISE 08

from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

# Min-max scaling function is used in the extra problem at the end of this lab
def min_max_scaling(X_train, X_test=None):     
    
    # Create a MinMaxScaler object that will compute min and max values
    scaler = MinMaxScaler()  

    # Fit the scaler on the training data (find min and max values for each feature)
    # Then transform the training data so each feature is scaled to the range [0, 1]                  
    X_train_scaled = scaler.fit_transform(X_train)  
    
    # Check if test data was provided
    if X_test is None:    
        # Return the scaled training data and an empty list for the test set           
        return X_train_scaled.tolist() + [] 

    # Use the SAME min and max values learned from the training set to scale the test data  
    # Important: we use transform(), not fit_transform(), so the test set does not affect scaling 
    X_test_scaled = scaler.transform(X_test)   

    # Return both scaled datasets converted to Python lists
    return X_train_scaled.tolist() + X_test_scaled.tolist()  

# PROBLEM 1
def perform_kmeans(X, n_clusters):
    """Run K-Means clustering (random_state=2500) and return the cluster labels as a list."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=2500)
    kmeans.fit(X)
    return kmeans.labels_.tolist()
# PROBLEM 2
def perform_hierarchical(X, n_clusters):
    """Run agglomerative clustering with average linkage and return the cluster labels as a list."""
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters, linkage='average')
    hierarchical.fit(X)
    return hierarchical.labels_.tolist()
# PROBLEM 3
def find_optimal_clusters(X, clustering_option="kmeans", max_k=10):
    """Find the number of clusters with the highest silhouette score."""
    best_score = -1
    best_k = 2

    for k in range(2, max_k + 1):
        if clustering_option == "kmeans":
            cluster_labels = perform_kmeans(X, k)
        else:
            cluster_labels = perform_hierarchical(X, k)

        score = silhouette_score(X, cluster_labels)
        score = float(score)

        print(f"Silhouette Score: {score:.3f}")

        if score > best_score:
            best_score = score
            best_k = k

    return best_k
# PROBLEM 4
def save_clustering_results(labels, filename):
    """Save cluster labels to a CSV file."""
    with open(filename, "w") as file:
        file.write("cluster_label\n")

        for label in labels:
            file.write(str(label) + "\n")
            
def main():
    data = load_iris()
    X = data.data.tolist()
    kmeans_labels = perform_kmeans(X, n_clusters=3)
    print(kmeans_labels)

    hierarchical_labels = perform_hierarchical(X, n_clusters=3)
    print(hierarchical_labels)
    
if __name__ == '__main__':
    main()
