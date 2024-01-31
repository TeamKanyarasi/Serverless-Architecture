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

