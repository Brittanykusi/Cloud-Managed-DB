## import packages
import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from faker import Faker # https://faker.readthedocs.io/en/master/
import uuid
import random

# connect to GCP server
load_dotenv()
GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USERNAME = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")

connection_string_gcp = f'mysql+pymysql://{GCP_MYSQL_USERNAME}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
db_gcp = create_engine(connection_string_gcp)

print(db_gcp.table_names())










### create fake data for conditions table

fake_conditions = """
insert into conditions (id, icd10_code, icd10_description) values (1, 'E08.37X1', 'Diabetes mellitus due to underlying condition with diabetic macular edema, resolved following treatment, right eye');"""

fake_conditions2 = """
insert into conditions (id, icd10_code, icd10_description) values (2, 'E03.4', 'Atrophy of thyroid');"""

fake_conditions3 = """
insert into conditions (id, icd10_code, icd10_description) values (3, 'C43.52', 'Malignant melanoma of skin of breast'),
(4, 'C73', 'Malignant neoplasm of thyroid gland'),
(5, 'G47.32 ', 'High altitude periodic breathing'),
(6, 'O30.1', 'Triplet pregnancy'),
(7, 'R07.1', 'Chest pain on breathing'),
(8, 'G50.1', 'Atypical facial pain'),
(9, 'R68.84', 'Jaw pain'),
(10, 'R10.0', 'Acute abdomen')
"""
db_gcp.execute(fake_conditions)
db_gcp.execute(fake_conditions2)
db_gcp.execute(fake_conditions3)










### create fake data for medications table
#### real ndc codes
ndc_codes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/FDA_NDC_CODES/main/NDC_2022_product.csv')
ndc_codes_100 = ndc_codes.sample(n=50, random_state=None)

# drop duplicates from ndc_codes_100
ndc_codes_100 = ndc_codes_100.drop_duplicates(subset=['PRODUCTNDC'], keep='first')

insertQuery = "INSERT INTO medications (med_ndc, med_human_name) VALUES (%s, %s)"

medRowCount = 0
for index, row in ndc_codes_100.iterrows():
    medRowCount += 1
    db_gcp.execute(insertQuery, (row['PRODUCTNDC'], row['NONPROPRIETARYNAME']))
    print("inserted row: ", index)
    ## stop once we have 50 rows
    if medRowCount == 51:
        break









### create fake data for patients_medications table
df_medications = pd.read_sql_query("SELECT med_ndc FROM medications", db_gcp) 
df_patients = pd.read_sql_query("SELECT mrn FROM patients", db_gcp)

# create a dataframe that is stacked and give each patient a random number of medications between 1 and 5
df_patients_medications = pd.DataFrame(columns=['mrn', 'med_ndc'])
# for each patient in df_patient_medications, take a random number of medications between 1 and 10 from df_medications and palce it in df_patient_medications
for index, row in df_patients.iterrows():
    # get a random number of medications between 1 and 5
    numMedications = random.randint(1, 5)
    # get a random sample of medications from df_medications
    df_medications_sample = df_medications.sample(n=numMedications)
    # add the mrn to the df_medications_sample
    df_medications_sample['mrn'] = row['mrn']
    # append the df_medications_sample to df_patient_medications
    df_patient_medications = df_patient_medications.append(df_medications_sample)

print(df_patient_medications.head(10))

# now lets add a random medication to each patient
insertQuery = "INSERT INTO patient_medications (mrn, med_ndc) VALUES (%s, %s)"

for index, row in df_patients_medications.iterrows():
    db_gcp.execute(insertQuery, (row['mrn'], row['med_ndc']))
    print("inserted row: ", index)










### create fake data for patients table
fake = Faker()

fake_patients = [
    {
        #keep just the first 8 characters of the uuid
        'mrn': str(uuid.uuid4())[:8], 
        'first_name':fake.first_name(), 
        'last_name':fake.last_name(),
        'zip_code':fake.zipcode(),
        'dob':(fake.date_between(start_date='-90y', end_date='-20y')).strftime("%Y-%m-%d"),
        'gender': fake.random_element(elements=('M', 'F')),
        'contact_mobile':fake.phone_number(),
        'contact_home':fake.phone_number()
    } for x in range(50)]
df_fake_patients = pd.DataFrame(fake_patients)

df_fake_patients.to_sql('patients', con=db_gcp, if_exists='append', index=False)










### create fake data for social_determinants table
loinc = """
insert into social_determinants (loinc_code, loinc_description) values ('87535-1', 'Challenges to maintaining treatments or health behaviors'), 
('93678-1', 'Have you been at the emergency department more than twice in the last 6 months [WellRx]'),
('74186-8', 'Health insurance funding was provided'),
('93680-7', 'Hospitalized in the last 6 months'),
('91653-6', 'How often is the following kind of support available to you if you need it - someone to take you to the doctor if you needed it [MOS Social Support Survey]'),
('68503-2', 'How well do you speak english [SAMHSA]'),
('52553-5', 'Language.primary is English'),
('92257-5', 'Number of visits with usual provider 12 months'),
('52556-8', 'Payment sources'),
('94066-8', 'Person-Centered Primary Care Measure [PCPCM]'),
('54899-0', 'Preferred language'),
('76437-3', 'Primary insurance'),
('68504-0', 'What language do you feel most comfortable speaking with your doctor or nurse [SAMHSA]')
"""

db_gcp.execute(loinc)










### create fake data for treatments_procedures table
cptcodes = pd.read_csv('https://gist.githubusercontent.com/lieldulev/439793dc3c5a6613b661c33d71fdd185/raw/25c3abcc5c24e640a0a5da1ee04198a824bf58fa/cpt4.csv')
list(cptcodes.columns)
newCPTcode = cptcodes.rename(columns={'com.medigy.persist.reference.type.clincial.CPT.code':'cpt_code', 'label':'cpt_description'})
newCPTcode.sample(n=100)

insertQuery = "INSERT INTO treatments_procedures (cpt_code, cpt_description) VALUES (%s, %s)"
startingRow = 0
for index, row in newCPTcode.iterrows():
    startingRow += 1
    print('startingRow: ', startingRow)
    # db_azure.execute(insertQuery, (row['CodeWithSeparator'], row['ShortDescription']))
    print("inserted row db_azure: ", index)
    db_gcp.execute(insertQuery, (row['cpt_code'], row['cpt_description']))
    print("inserted row db_gcp: ", index)
    ## stop once we have 100 rows
    if startingRow == 60:
        break