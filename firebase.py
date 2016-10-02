from firebase import Firebase
from firebase_token_generator import create_token
import pprint
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np
from sklearn.cluster import KMeans
import random
from random import choice
from string import ascii_uppercase
import json

#test clustering with random data


base_url = "https://personality-recommender-80814.firebaseio.com/"
users_url = base_url + 'users'

auth_payload = {"uid": "lfeqCjaPdHdML4Jtgri23RFVzBm1"}
secret_key = "1G8cEGmnVLb20kWnpkmac3cSvEy1NZKJu0BJ0pRR"
options = {
        "debug": True,
        "admin": True
}

token = create_token(secret_key, auth_payload, options)
ref = Firebase(base_url, auth_token = token)
users_ref = Firebase(users_url, auth_token = token)



if __name__ == '__main__':
    data = users_ref.get()
    sample = data['qu yaoxian']
    pprint.pprint(data)
    for i in range(90):
        name = ''.join(choice(ascii_uppercase) for i in range(12))
        for i in range(5):
            sample["tree"]["children"][2]["children"][0]["children"][i]["percentage"] = random.uniform(0, 1)
        users_ref.patch({name: sample})

    # all_users = users_ref.get()
    # values_arr = [ {key: all_users[key]["tree"]["children"][2]["children"][0]["children"]} for key in all_users]

    # for i in range(100):
    #     values_arr.append({''.join(choice(ascii_uppercase) for i in range(12)): [{u'category': u'values',
    #                u'id': u'Conservation',
    #                u'name': u'Conservation',
    #                u'percentage': random.uniform(0, 1),
    #                u'sampling_error': 0.0694932559},
    #               {u'category': u'values',
    #                u'id': u'Openness to change',
    #                u'name': u'Openness to change',
    #                u'percentage': random.uniform(0, 1),
    #                u'sampling_error': 0.0656537209},
    #               {u'category': u'values',
    #                u'id': u'Hedonism',
    #                u'name': u'Hedonism',
    #                u'percentage': random.uniform(0, 1),
    #                u'sampling_error': 0.1402586488},
    #               {u'category': u'values',
    #                u'id': u'Self-enhancement',
    #                u'name': u'Self-enhancement',
    #                u'percentage': random.uniform(0, 1),
    #                u'sampling_error': 0.1057336045},
    #               {u'category': u'values',
    #                u'id': u'Self-transcendence',
    #                u'name': u'Self-transcendence',
    #                u'percentage': random.uniform(0, 1),
    #                u'sampling_error': 0.0838543583}]})


    # num_users = len(values_arr)
    # num_features = 5

    # values_m = dok_matrix((num_users, num_features), dtype=np.float32)

    # for i in range(num_users):
    #     for j in range(num_features):
    #         for key in values_arr[i]:
    #             values_m[i, j] = values_arr[i][key][j]["percentage"]


    # k = int(num_users / 10) + 2
    # kmeans = KMeans(n_clusters = k)
    # clustering = kmeans.fit(values_m.tocsr())
    
    # rec_list_loc = []
    # rec_list = []
    # #assume current user is on line 0, have to find out actual user position
    # for i, cluster_label in enumerate(clustering.labels_):
    #     if(cluster_label == clustering.labels_[0] and i != 0):
    #         rec_list_loc.append(i)

    # for i in rec_list_loc:
    #     for key in values_arr[i]:
    #         rec_list.append(key)

    # print(rec_list)


