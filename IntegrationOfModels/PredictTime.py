from joblib import load
import pandas as pd

# Initialize an dictionary to store ward names and IDs
ward_names_to_ids= {
    "Kempegowda Ward": 1,
    "Chowdeshwari Ward": 2,
    "Atturu Ward": 3,
    "Yelahanka Satellite Town Ward": 4,
    "Kogilu Ward": 162,
    "Jakkuru Ward": 5,
    "Thanisandra Ward": 6,
    "Amrutahalli Ward": 152,
    "Hebbal Kempapura Ward": 198,
    "Byatarayanapura Ward": 7,
    "Kodigehalli": 8,
    "Dodda Bommasandra": 10,
    "Vidyaranyapura": 9,
    "Kuvempu Nagar": 11,
    "Kammagondanahalli": 28,
    "Mallasandra": 13,
    "Chikkasandra": 39,
    "Bagalakunte": 14,
    "T Dasarahalli": 15,
    "Nalagadarenahalli": 197,
    "Chokkasandra": 38,
    "Peenya Industrial Area": 41,
    "Rajagopal Nagar": 70,
    "Hegganahalli": 71,
    "Sunkadakatte": 196,
    "Dodda Bidarakallu": 40,
    "Lingadheeranahalli": 49,
    "Herohalli": 72,
    "Ullalu": 130,
    "Nagadevanahalli": 67,
    "Bande Mutt": 195,
    "Kengeri": 159,
    "Hemmigepura": 128,
    "JP Park": 17,
    "Yeshwanthpura": 37,
    "Jalahalli": 16,
    "Peenya": 194,
    "Laxmidevi Nagar": 42,
    "Laggere": 69,
    "Chowdeshwari Nagar": 193,
    "Kottegepalya": 73,
    "Srigandhadakaval": 192,
    "Malathalli": 191,
    "Jnana Bharathi": 129,
    "Rajarajeshwari Nagar": 160,
    "Rajiv Nagar": 190,
    "Mahalakshmipuram": 68,
    "Nagapura": 67,
    "Nalvadi Krishna Raja Wadiyar": 189,
    "Shankar Matt": 75,
    "Shakthi Ganapathi Nagar": 74,
    "Vrisabhavathi Nagar": 102,
    "Mattikere": 36,
    "Malleswaram": 45,
    "Aramane Nagara": 145,
    "Rajamahal Guttahalli": 64,
    "Kadu Malleshwara": 65,
    "Subramanya Nagar": 66,
    "Gayithri Nagar": 76,
    "Radhakrishna Temple": 18,
    "Sanjaya Nagar": 19,
    "Hebbala": 21,
    "Vishwanath Nagenahalli": 22,
    "Manorayanapalya": 33,
    "Chamundi Nagara": 188,
    "Ganga Nagar": 34,
    "Jayachamarajendra Nagar": 46,
    "Kaval Bairasandra": 32,
    "Kushal Nagar": 31,
    "Muneshwara Nagar": 48,
    "Devara Jeevanahalli": 47,
    "S K Garden": 61,
    "Sagayarapuram": 60,
    "Pulikeshinagar": 78,
    "Hennur": 187,
    "Nagavara": 23,
    "HBR Layout": 24,
    "Kadugondanahalli": 30,
    "Kacharkanahalli": 29,
    "Kammanahalli": 28,
    "Banasavadi": 27,
    "Subbayyanapalya": 186,
    "Lingarajapura": 49,
    "Begur": 185
}



#print(ward_names_to_ids)

# Load the model from the file
rf_model = load(r"D:/Btech_AI/4thsem/AI/Project/IntegrationOfModels/random_forest_model.joblib")

pd.pandas.set_option('display.max_columns',None)
df = pd.read_csv(r"D:/Btech_AI/4thsem/AI/Project/IntegrationOfModels/data.csv")
# one-hot encoding categorical variables
df = pd.get_dummies(df, columns=['sourceid', 'destid']) 

X = df.drop(['duration', 'duration_in_traffic'], axis=1)
y = df[['duration', 'duration_in_traffic']]

def predict_travel_timesL(sourceid, destid):
    # Create a new DataFrame with the same structure as X
    X_new = pd.DataFrame(columns=X.columns)
    
    # Add the sourceid and destid to the new DataFrame
    X_new.loc[0, f'sourceid_{sourceid}'] = 1
    X_new.loc[0, f'destid_{destid}'] = 1
    
    # Fill any NaN values with 0
    X_new = X_new.fillna(0)
 
    
    # Make predictions
    y_pred = rf_model.predict(X_new)
    
    # Return the predictions
    return y_pred[0]

def get_predicted_times(source_ward, dest_ward):
    source_id = ward_names_to_ids[source_ward]
    dest_id = ward_names_to_ids[dest_ward]
    predictions = predict_travel_timesL(source_id, dest_id)
    return predictions

sourceid = int(input("Enter SourceID: "))
destid = int(input("Enter DestinationID: "))
predictions = predict_travel_timesL(sourceid, destid)
print(f'Predicted travel time in normal hours: {predictions[0]}')
print(f'Predicted travel time in peak traffic hours: {predictions[1]}')