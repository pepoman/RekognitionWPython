import boto3
import json

if __name__ == "__main__":
    photo='smile.jpg'
    bucket='palacang.com'
    client=boto3.client('rekognition')

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        print('The detected mood is  ' + str(faceDetail['Emotions'][0]['Type']))
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
