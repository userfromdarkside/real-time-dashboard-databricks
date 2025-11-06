1. create and activate a new env
python -m venv env_s3_streaming ;
.\env_s3_streaming\Scripts\activate

2. create an IAM user which has a full s3access ;
Download the credentials csv file

2. connect to s3
aws configure

3. run and test the streaming

4. read data directly from s3 instead of mounting it

4. generate databricks access token : dapiccbfd5b915d26e2d383aa6fc6e9e2a98

5. install databricks CLI

7. setup databricks secrets scopes for s3 so I dont need to run again