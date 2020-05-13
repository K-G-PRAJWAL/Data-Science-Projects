import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


# Pass form data to prediction model
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():  # Load the pickle and json file
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # locations start from 4 column

    global __model
    if __model is None:
        with open('./artifacts/Bengaluru_House_Data.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
