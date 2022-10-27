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

### Step 4. Create a python script called (sql_dummy_data.py) using python and send some dummy data into each of the tables.
- in your script make sure to 
    - import all packages https://github.com/Brittanykusi/Cloud-Managed-DB/blob/a666366deb93d81d8b6ef372bf386d1dd78e45ac/sql_dummy_data.py#L2-L10
    - connect to server https://github.com/Brittanykusi/Cloud-Managed-DB/blob/3ffc8345aba8c85ac0f9b4ec8e5944ce94ac9a28/sql_table_creation.py#L9-L17
    - create dummy data (fake data input) https://github.com/Brittanykusi/Cloud-Managed-DB/blob/061d5bf79b4b342e4288d7ba2700925b9489f81e/script/sql_dummy_data.py#L127-L143
    - create dummy data (manual input) https://github.com/Brittanykusi/Cloud-Managed-DB/blob/061d5bf79b4b342e4288d7ba2700925b9489f81e/script/sql_dummy_data.py#L35-L53
    - create dummy data (other input) https://github.com/Brittanykusi/Cloud-Managed-DB/blob/061d5bf79b4b342e4288d7ba2700925b9489f81e/script/sql_dummy_data.py#L66-L81

#### Step 4b. Connect to MySQL on computer terminal
- simple way
    - run ``` sudo mysql -u root -h 34.171.172.227 -p ``` 
-if you run into this error " mysql not found " install homebrew via [install homebrew](https://brew.sh/) on your personal terminal
    - you shuld then be able to run the above command
    - if it doesnt work you will need to locate mysql on you device
        - once you find the location/path run ``` sudo nano /etc/paths ``` and insert the path followed my mysql or myslqsh
        - save and exit nano
        - you should now be able to use the above command

### Step 5. Create an ERD for your DB design using MySQL Work Bench. You must have at least two foreignKeys representing a relationship between at least 2 tables. 
- enter your application
- connect to db
    - click the (+) icon near mysql connections 
    - create a connection name 
    - input the host name, port, and username of your cloud server instance
    - click okay and you will be prompted to input your password
- create ERD diagram
    -  click database at the top of your homescreen
    -  navigate to reverse engineer
    -  select the stored connection name
    -  select the db
    -  execute

