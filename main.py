import pypickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data=pypickle.load('train.pkl')


st.title('smoker prediction')
age =st.number_input('How old are you?')
amt_weekends=st.number_input('Amount of cigarette smoked on weekends?')
amt_weekdays= st.number_input('Amount of cigarette smoked on weekdays?')

gender =st.radio('Select your gender : ', ('Male','Female'))
if gender == 'Male':
    gender = st.text_input('Male')
elif (gender == 'Female'):
    # take gender input in text
     gender = st.text_input('Female')

marital_status=st.radio('Select your marital status: ', ('Single','Married','Divorced'))
if marital_status == 'Single':
    marital_status= st.text_input('Single')
elif(marital_status == 'Married'):
    # take gender input in text
     marital_status = st.text_input('Married')
elif (marital_status == 'Divorced'):
    # take gender input in text
     marital_status = st.text_input('Divorced')


highest_qualification=st.radio('Select your highest qualification:', ('No qualification','Degree','A level'))
if highest_qualification == 'No qualification':
    highest_qualification = st.text_input('No qualification')
elif (highest_qualification == 'Degree'):
    # take gender input in text
     highest_qualification = st.text_input('Degree')
elif (highest_qualification== 'A level'):
    # take gender input in text
     highest_qualification = st.text_input('A level')

nationality=st.radio('Nationality:', ('British','English','Scotish'))
if nationality == 'British':
    nationality = st.text_input('British')
elif (nationality == 'English'):
    # take gender input in text
     nationality = st.text_input('English')
elif (nationality == 'Scotish'):
    # take gender input in text
     nationality = st.text_input('Scotish')

ethnicity=st.radio('ethnicity:', ('White','Black','Chinese'))
if ethnicity== 'White':
    ethnicity = st.text_input('White')
elif (ethnicity == 'Black'):
    # take gender input in text
      ethnicity= st.text_input('Black')
elif (ethnicity == 'Chinese'):
    # take gender input in text
     ethnicity = st.text_input('Chinese')

gross_income=st.number_input('What is your gross income?')

type=st.radio('type:', ('Packets','hand_rolled'))
if type == 'Packets':
    type = st.text_input('packets')
elif (type == 'Hand_rolled'):
    # take gender input in text
     type = st.text_input('Hand_rolled')

region=st.radio('region:', ('South east','South west','London'))
if region == 'South east':
    region = st.text_input('South east')
elif (region == 'South west'):
    # take gender input in text
      region= st.text_input('South west')
elif (region == 'London'):
    # take gender input in text
     region = st.text_input('London')


#encoder=['age', 'amt_weekends','amt_weekdays','gender','marital_status',
          #'highest_qualification','nationality','ethnicity','gross_income','region','type']

x=pd.DataFrame({

    'age': [age],
    'amt_weekends': [amt_weekends],
    'amt_weekdays': [amt_weekdays],
    'gender': [gender],
    'marital_status': [marital_status],
    'highest_qualification': [highest_qualification],
    'nationality': [nationality],
    'ethnicity': [ethnicity],
    'gross_income': [gross_income],
    'region': [region],
    'type': [type]

})

encoder= LabelEncoder()


#Label Encoder to convert categorical columns into numerical features passing in a lambda function
def object_to_int(dataframe_series):
    if dataframe_series.dtype=='object':
        dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series

df_merges = x.apply(lambda x: object_to_int(x))
df_merges.head()

if (st.button('Predict likelihood to become a smoker')):
    predict= data.predict(df_merges)
    if predict== 1:
        st.write('yes')
    else:
        st.write('No')