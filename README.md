# real-time-dashboard-databricks

<img width="1170" height="656" alt="image" src="https://github.com/user-attachments/assets/9d85ad70-23e7-41a4-af61-490b0711e9af" />


### step 1: write a python script to simulate the json files streaming
you can find the python script in the main.py file above
one thing I really like about dataclass is I can expand it easily
<img width="1025" height="555" alt="image" src="https://github.com/user-attachments/assets/edad0f32-07a5-412e-b87d-b187065e6548" />

### step 2: create an AWS IAM user 
-> genereate access secret -> download the credential

### step : create a S3 bucket
here is the image when i test the streaming between VS Code and S3
<img width="1476" height="735" alt="image" src="https://github.com/user-attachments/assets/9d70bf38-1cfe-4626-959c-46758622e31f" />

### step 3: connect VS Code to the S3 via the Iam user credential

### step 4: create a premium Databricks workspace 
there are some reasons why I use Databricks premium:
- I need to read cloud files from S3 and Databricks free edition doesn't support
- where i create an all-purpose cluster for my notebook I observed the limitation in vCPUs. So I need the premium account to request increasing computes

### step 5: connect Databricks to S3
instead of hardcoding, I prefer to use Databricks CLI and then setup the databricks secret scope.

### step 6: create a notebook to read data from s3
<img width="1163" height="831" alt="image" src="https://github.com/user-attachments/assets/45ab1dd9-9a44-4f56-a541-4c5aefeec5e0" />
you can find the notebook above

### step 7: create a dlt pipeline
the interesting thing about declerative pipelines is you dont need to define the workflow, you just need to write the code and Databricks will do the ochestration for you
<img width="1600" height="854" alt="image" src="https://github.com/user-attachments/assets/3007f87b-9ce3-40fa-b02e-f0cf46b2be26" />
I create stream tables so I can get near realtime data for my streaming dashboard. Why I said it is near realtime ? because it also depends on the compute size and also the time that my queries take
remember to change the schedule option from triggered to continuous

### step 8: connect to power bi
run the sql warehouse compute -> go to endpoint -> download the connection for Power BI
remember to change the refresh time of the dashboard to 1 second so you can see the new data right after it arrives

--- that's it, thanks for visiting my project
