# RekognitionWPython
A simple test of Rekognition AWS function with Python, as of first version it only detects the mood giving an image filename and bucket in S3 that is specified in mood.py 

Following Steps:
Add picture location functions


Implementation Aspects:

• Define API
Implementation is done using Boto 3.
Boto is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2. Boto provides an easy to use, object-oriented API as well as low-level direct service access.

(more info here https://boto3.readthedocs.io/en/latest/)

• Layout code structure
With command “aws rekognition detect-faces –generate-cli-skeleton” we can get an example-skeleton JSON format to request the data that is required according to our needs. 
{
    "Image": {
        "Bytes": null,
        "S3Object": {
            "Bucket": "",
            "Name": "",
            "Version": ""
        }
    },
    "Attributes": [
        "DEFAULT"
    ]
}

• Design data model and key data structures

Local Backend Design
Image Upload → S3 Bucket → local Python script → Rekognition Invoked in AWS → JSON return of desired informatión

Lamda Design
Image Upload → S3 Bucket → Rekognition Blueprint Lamda →  Output sent to CloudWatch log streams → Publish  ARN with SNS

• Define data persistence using any data store of your choice.
Data store is being handled by Amazon’s S3 bucket service so we can assure data is available all time.


• Define Implementation of operations
Operation costs for S3 Buckets and Lambda functions are really low, according to AWS pricing
Duration of request $0.00000625125 for every 128MB-second 

• Input validation
Rekognition works by default with jpeg, jpg and png images with a limit size of 5MB

• Authentication
Authentication is made with aws configure from source environment, also there is a way to use a lamda function to process with Rekognize everytime a new image is uploaded to an specified S3 bucket. In this case authentication can be made thru Amazon GUI console or CLI

• Authorization
Authorization has to be made from initial setup for the required user to be added into the respective policy groups



