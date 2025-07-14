#transform_json_to_csv.py

import json
import pandas as pd



def get_dataframe(data):
    """
    Transform the data into a DataFrame
    """
    with open(data) as f:
        data = json.load(f)

    list_of_keys = []

    for element in data:
        for key in element.keys():
            if not isinstance(element[key], dict) and key not in list_of_keys:
                list_of_keys.append(key)
            elif isinstance(element[key], dict):
                for subkey in element[key].keys():
                    if not isinstance(element[key][subkey], dict) and f"{key}%%{subkey}" not in list_of_keys:
                        list_of_keys.append(f"{key}%%{subkey}")
                    elif isinstance(element[key][subkey], dict):
                        print(key,subkey,element[key][subkey])


    df_source = {key.replace('%%', '_') : [] for key in list_of_keys}

    for element in data:
        keys = element.keys()
        for key in list_of_keys:
            if '%%' not in key:
                if key in keys:
                    df_source[key].append(element[key])
                else:
                    df_source[key].append(None)
            else:
                new_key, sub_key = key.split('%%')
                if new_key in keys:
                    sub_keys = element[new_key].keys()
                    if sub_key in sub_keys:
                        df_source[key.replace('%%', '_')].append(element[new_key][sub_key])
                    else:
                        df_source[key.replace('%%', '_')].append(None)
                else:
                    df_source[key.replace('%%', '_')].append(None)

    return pd.DataFrame(df_source)

    

def transform_dataframe(df):
    """
    Opérations de transformation des données dans le DF
    """
    df['personal_gender'] = df['personal_gender'].replace({'female': 'F', 'Female': 'F', 'male': 'M', 'Male': 'M'})
    df.loc[df['personal_age'] < 0, 'personal_age'] = -df.loc[df['personal_age'] < 0, 'personal_age']

    avg_age_child = df[(df['personal_age'] <= 17) & (df['personal_age'] > 0)]['personal_age'].mean()
    avg_age_adult = df[(df['personal_age'] >= 18)]['personal_age'].mean()
    df.loc[(df['personal_marital_status'].isna()) & (df['personal_age'] == 0), 'personal_age'] = avg_age_child
    df.loc[df['personal_age'] == 0, 'personal_age'] = avg_age_adult

    df.loc[df['personal_age'] < 18, 'personal_marital_status'] = "Single"
    # pmsm = df[df['personal_age'] >= 18]['personal_marital_status'].mode()[0]
    df['personal_marital_status'] = df['personal_marital_status'].replace({'': 'Single'})

    eelm = df[(df['experience_education_level'] != '') & (df['personal_age'] >= 18)]['experience_education_level'].mode()[0]
    df.loc[df['personal_age'] < 18, 'experience_education_level'] = 'High School'
    df.loc[(df['personal_age'] >= 18) & (df['experience_education_level'] == ''), 'experience_education_level'] = eelm

    df_na = df.dropna()

    return df_na



if __name__ == "__main__":
    df = get_dataframe('./data/data.json')
    df = transform_dataframe(df)

    # Save
    df.to_csv('./data/people.csv', index = False)