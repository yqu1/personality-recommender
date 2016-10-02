from firebase import Firebase
from firebase_token_generator import create_token
import pprint
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np
from sklearn.cluster import KMeans


def get_clusters(users_ref):
    all_users = users_ref.get()
    values_arr = [ {key: all_users[key]["tree"]["children"][2]["children"][0]["children"]} for key in all_users]

    num_users = len(values_arr)
    num_features = 5

    values_m = dok_matrix((num_users, num_features), dtype=np.float32)

    for i in range(num_users):
    	for j in range(num_features):
    		for key in values_arr[i]:
    			values_m[i, j] = values_arr[i][key][j]["percentage"];
	k = int(num_users / 10) + 2
	kmeans = KMeans(n_clusters = k)

	clustering = kmeans.fit(values_m.tocsr())
	return clustering
