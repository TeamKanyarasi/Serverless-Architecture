# Serverless-Architecture

## TASK 1: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3.
### Objective:
To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket older than 30 days.

#### 1. S3 Setup:

   - Navigate to the S3 dashboard and create a new bucket.

   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

![Screenshot (94)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/12dcb091-0fc4-422f-9334-12ceab6f91ac)

#### 2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

#### 3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

![Screenshot (98)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/654cb61b-d832-4f7b-8015-4203b5494603)

#### 4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Go to the S3 dashboard and confirm that only files newer than 30 days remain.

![Screenshot (95)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/44e8c59f-e635-4e54-99e0-68f6d3e1befb)

![Screenshot (97)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/6b46dce6-cd00-4fa7-b355-d4745b7b28ea)

## TASK 2: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3.
### Objective:
Learn to automate the tagging of EC2 instances as soon as they are launched, ensuring better resource tracking and management.

#### 1. EC2 Setup:

   - Ensure you have the capability to launch EC2 instances.

#### 2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonEC2FullAccess` policy to this role.

#### 3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.
     4. Print a confirmation message for logging purposes.

#### 4. CloudWatch Events:

   - Set up a CloudWatch Event Rule to trigger on the EC2 instance launch event.

   - Attach the Lambda function as the target.

#### 5. Testing:

   - Launch a new EC2 instance.

   - After a short delay, confirm that the instance is automatically tagged as specified.

## TASK 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3.
### Objective:
To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side encryption.

#### 1. S3 Setup:

   - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.

#### 2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3ReadOnlyAccess` policy to this role.

#### 3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List all S3 buckets.
     3. Detect buckets without server-side encryption.
     4. Print the names of unencrypted buckets for logging purposes.

![Screenshot (100)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/8d12713e-1f30-455a-9d27-cb81a72f6ede)

#### 4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Review the Lambda logs to identify the buckets without server-side encryption.

![Screenshot (99)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/985e5c82-66cc-4f65-b44e-8a3712f695c4)

## TASK 4: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS.
### Objective:
Automatically monitor changes in EC2 instance states and send notifications whenever an instance is started or stopped.

#### 1. SNS Setup:

   - Navigate to the SNS dashboard and create a new topic.

   - Subscribe to this topic with your email.

#### 2. Lambda IAM Role:

   - Create a role with permissions to read EC2 instance states and send SNS notifications.

#### 3. Lambda Function:

   - Create a function and assign the above IAM role.

   - Use Boto3 to:

     1. Extract details from the event regarding the EC2 state change.
     2. Send an SNS notification with details about which EC2 instance changed state and the new state (e.g., started, stopped).

![Screenshot (92)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/e66dc2f2-9f98-45cd-b02d-68d7dc381760)

![Screenshot (91)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/bf7b5ad8-9689-4f9e-8e07-8378126b76d4)

#### 4. EC2 Event Bridge (formerly CloudWatch Events):

   - Set up an Event Bridge rule to trigger your Lambda function whenever an EC2 instance state changes.

![Screenshot (93)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/a9d602b5-f33d-4cbe-bdbc-3462d74dd75b)

#### 5. Testing:

   - Start or stop one of your EC2 instances.

   - Confirm you receive an SNS notification about the state change.

![Screenshot (90)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/ae427934-de5f-4e57-8969-cb9a4db5d328)

## TASK 5: Load Balancer Health Checker.
### Objective:
Design a Lambda function that checks the health of registered instances behind an Elastic Load Balancer (ELB) and notifies via SNS if any instances are unhealthy.

1. Create a Lambda function.

![Screenshot (84)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/e441ad08-c9f2-4237-83d3-40e421ec2989)

![Screenshot (85)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/08ca2e0d-7aa9-4b95-999d-d2a401383a73)

![Screenshot (86)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/d209f9f2-da0d-4455-adc8-676893b74ff6)

2. With Boto3, configure the function to:

3. Check the health of registered instances behind a given ELB.

![Screenshot (89)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/af63e0d2-d0c0-4349-9d8e-2453bd76519b)

4. If any instances are found to be unhealthy, publish a detailed message to an SNS topic.

5. Set up a CloudWatch event to trigger this Lambda function every 10 minutes.

![Screenshot (87)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/5bcabbf6-b618-470b-9eab-8e7e5a9abf44)

![Screenshot (88)](https://github.com/TeamKanyarasi/Serverless-Architecture/assets/139607786/521facce-457a-46db-96ae-d6f03c54db62)
