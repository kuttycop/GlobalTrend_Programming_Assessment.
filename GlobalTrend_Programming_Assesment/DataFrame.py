import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
def preprocess_data(df):
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )
    df_processed = preprocessor.fit_transform(df)
    num_features = numerical_cols
    cat_features = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols)
    feature_names = list(num_features) + list(cat_features)
    df_processed = pd.DataFrame(df_processed, columns=feature_names)

    return df_processed

# Example Inputs
data = {
    'age': [25, 30, 35, 40, None],
    'income': [50000, 60000, 70000, 80000, 90000],
    'gender': ['male', 'female', None, 'female', 'male'],
    'city': ['New York', 'Los Angeles', 'Chicago', None, 'New York']
}
df = pd.DataFrame(data)
cleaned_df = preprocess_data(df)
print(cleaned_df)