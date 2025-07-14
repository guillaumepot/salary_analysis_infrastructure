# src/docker/prepare_dataframe/prepare_dataframe.py


import pandas as pd

def read_df(filepath):
    """
    Load a CSV file into a DataFrame
    """
    return pd.read_csv(filepath)

def transform_df(df):
    """
    Apply transformations to the DF
    """
    col_to_keep = ['id', 'company_name', 'personal_gender',
                   'job_salary', 'job_position_level',
                   'job_performance_score', 'job_last_promotion_date',
                   'job_work_hours_per_week','experience_experience_years',
                   'experience_has_certifications'
                   ]

    new_col_names = {'company_name': 'company',
                     'personal_gender': 'gender',
                     'job_salary': 'salary',
                     'job_position_level': 'position_level',
                     'job_performance_score': 'performance_score',
                     'job_last_promotion_date': 'last_promotion_date',
                     'job_work_hours_per_week': 'work_hours_per_week',
                     'experience_experience_years': 'experience_years',
                     'experience_has_certifications': 'has_certifications',
                     }

    df = df[col_to_keep]
    df = df.rename(columns = new_col_names)
    df["promoted"] = ~df["last_promotion_date"].isna()

    company_replace = {"Apple": 4, "Google": 3, "Amazon": 2, "Facebook": 1, "Microsoft": 0}
    position_replace = {"Senior": 2, "Mid": 1, "Junior": 0}
    gender_replace = {"M": 1, "F": 0}
    df = df.replace(company_replace)
    df = df.replace(position_replace)
    df = df.replace(gender_replace)

    # This column causes issues (dates are not in the same format: YYYY-MM-DD and DD-MM-YYYY)
    df = df.drop('last_promotion_date', axis = 1)

    return df



if __name__ == "__main__":
    df = read_df('./data/people.csv')
    df = transform_df(df)

    # Save
    df.to_csv('./data/prepared_people.csv', index = False)