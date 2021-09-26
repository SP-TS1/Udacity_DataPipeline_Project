# Sparkify Project
### Data Pipelines with Airflow

#### Project Summary
The project follows the follow steps:
* Step 1: Scope the project data
* Step 2: Setup Airflow connections with AWS
* Step 3: Configure the DAG and structure the operators
* Step 4: Run ETL and monitor processes on Airflow UI
* Step 5: Complete Project Write Up

_________________

### Step 1: Scope the project data

#### Scope 
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.
The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to. So in this project will give practical experiences of creating custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step. 

_________________

### Step 2: Setup Airflow connections with AWS
#### 2.1 Create Redshift Cluster on AWS
* Build IAM Role and give access authorities.
* Build Redshift Cluster using AWS console.
* Config Redshift to be able to accessed by role created .

#### 2.2 Create connections in Airflow
* Build aws_credentials (Conn ID) to connect to AWS console by using ACCESS_KEY_ID and SECRET_ACCESS_KEY.
* Build redshift (Conn ID) to connect Airflow with Redshift Cluster on AWS.
_________________

### Step 3: Configure the DAG and structure the operators
#### 3.1 Configure the DAG
1. Start the project by preparing all the tables where we will store data on Redshift.
2. Extract JSON formatted files from S3 to Redshift in stage_events and stage_songs.
3. Transform data into fact tables then insert formatted data to each dimension tables.
4. Check the data quality after all insertion.

#### 3.2 Structure operators in the DAG
##### Start Operator
   The start operator is the first operator that would be executed, the main purpose is to prepare all the tables in redshift which would be filled later by data from staging events in S3 buckets. If Redshift cluster have already had any tables on them, the function should delete and re-create them again.

##### Stage Operator
   The stage operator is expected to be able to load any JSON formatted files from S3 to Amazon Redshift. The operator creates and runs a SQL COPY statement. The operator's parameters should specify where in S3 the file is loaded and what is the target table.

   The parameters should be used to distinguish between JSON file. Another important requirement of the stage operator is containing a templated field that allows it to load timestamped files from S3 based on the execution time and run backfills.

##### Fact and Dimension Operators
   With dimension and fact operators, we could take as input a SQL statement and target database on which to run the query against in order to insert data into every tables within the Redshift cluster. Dimension loads are often done with the truncate-insert pattern where the target table is emptied before the load but Fact tables are usually so massive that they should only allow append type functionality.

##### Data Quality Operator
   The final operator is the data quality operator, which is used to run checks on the data itself. The operator's main functionality is to receive one or more SQL based test cases along with the expected results and execute the tests. For each the test, the test result and expected result needs to be checked and if there is no match, the operator should raise an exception and the task should retry and fail eventually.

_________________

### Step 4: Run ETL and monitor processes on Airflow UI
#### 4.1 Run ETL
* Use Airflow UI to start and run the DAG.
* Monitor DAG whether the processes ran with no troubles.
#### 4.2 Data Quality Checks
* Check quality of the data by finding NULL in primary key of each tables.

_________________

#### Step 5: Complete Project Write Up
#### choice of tools and technologies for the project
   In this project I chose postgresql to handle the data on Redshift because it's easier to cope with not very large data and also not using complex queries, But I mainly focused on practing to use Airflow such as creating custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data. Also using Airflow UI is much easier to monitor processes in the pipelines since there are DAG graph and logs for checking. Apart from this, Python is an often used programming language and was used because it is the language I am the most comfortable with.
    
_________________
