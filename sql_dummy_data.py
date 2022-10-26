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
fake = Faker()

fake_medications = 
### create fake data for patients_medications table
fake = Faker()

fake_patients_medications = 

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

# drop duplicate mrn
df_fake_patients = df_fake_patients.drop_duplicates(subset=['mrn'])

### create fake data for social_determinants table
fake = Faker()

fake_social_determinants = 
### create fake data for treatments_procedures table
fake = Faker()

fake_treatments_procedures = 






df_fake_patients = pd.DataFrame(fake_patients)
# drop duplicate mrn
df_fake_patients = df_fake_patients.drop_duplicates(subset=['mrn'])