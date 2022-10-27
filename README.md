# Cloud-Managed-DB
Objective: to create a relational database using cloud services.
Needed Applications:
- VSCode
- MySQL Workbench
- Github Desktop
- GCP or Azure account (this repo will be using GCP for MySQL use)

### Step 1: Create a cloud-managed MySQL DB on GCP
- log into GCP account
- search and select SQL and create instance 
- select MySQL
- fill in ID name and password (rememebr password)
- change machine type to lightweight and create instance
- once instance has been created navigate to connections on the left-side pane
- scroll to the bottom and add network 
- name your network and add 0.0.0.0/0 and save

### Step 2. Create a new database inside of that mysql instance called patient_portal  
- navigate to databases
- choose a name and create 

### Step 3. Create a python script called (sql_table_creation.py) that creates the following tables inside of patient_portal: patients, medications, treatments_procedures, conditions, and social determinants. Be sure to use a .env file to hide your login credentials 
- in your script make sure to 
    - import all packages https://github.com/Brittanykusi/Cloud-Managed-DB/blob/3ffc8345aba8c85ac0f9b4ec8e5944ce94ac9a28/sql_table_creation.py#L2-L7
    - connect to server https://github.com/Brittanykusi/Cloud-Managed-DB/blob/3ffc8345aba8c85ac0f9b4ec8e5944ce94ac9a28/sql_table_creation.py#L9-L17
    - create tables (example) https://github.com/Brittanykusi/Cloud-Managed-DB/blob/3ffc8345aba8c85ac0f9b4ec8e5944ce94ac9a28/sql_table_creation.py#L20-L33

### Step 4. Create a python script called (sql_dummy_data.py) using python and send some dummy data into each of the tables. Please see notes for ideas related to dummy data. 

### Step 4b. Connect to MySQL on computer terminal
- simple way
-if you run into this error

### Step 5. Create an ERD for your DB design using MySQL Work Bench. You must have at least two foreignKeys representing a relationship between at least 2 tables. 

6. Github docs to include: 
- a readme file that describes a) where you setup the mySQL db, b) any issues you ran into 
- a images folder that contains: 
    - screen shot of a ERD of your proposed setup (use either popSQL or mysql work bench) 
    - screen shots of you connected to the sql server, performing the following queries: 
        - Query1: show databases (e.g., show databases;) 
        - Query2: all of the tables from your database (e.g., show tables;)  
        - Query3: select * from patient_portal.medications 
        - Query4: select * from patient_portal.treatment_procedures
        - Query5: select * from patient_portal.conditions

Be CREATE with your dummy data and find examples that are from real-world codexes: 
Medications: NDC codes
Treatments/Procedures: CPT 
Conditions: ICD10 codes
Social_Determinants: LOINC codes 

Resources to pull some test data: 
NDC: https://dailymed.nlm.nih.gov/dailymed/index.cfm 
CPT: https://www.aapc.com/codes/cpt-codes-range/
ICD: https://icdcodelookup.com/icd-10/codes
LOINC: https://www.findacode.com/loinc/LG41762-2--socialdeterminantsofhealth.html

REAL CPT Values that are older: https://gist.github.com/lieldulev/439793dc3c5a6613b661c33d71fdd185
