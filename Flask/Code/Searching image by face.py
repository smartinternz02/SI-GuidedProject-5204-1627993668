import boto3
import csv

with open("new_user_credentials.csv",'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[0]
        secret_access_key = line[1]
        session_token = line[2]
        
client = boto3.client('rekognition',
                      aws_access_key_id ="AKIAVSOODXZIA2N63CAP",
                      aws_secret_access_key ="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",
                      region_name ='us-east-1'
                        )

def main():
    bucket = 'intelligentalbum'
    collection_id = 'Intelligent_Album_ManageRR'
    
    fileNames = ['test5.jpg']
    threshold =70
    maxFaces = 2
    
    for fileName in fileNames:
        response=client.search_faces_by_image(CollectionId=collection_id,
                                              Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                              FaceMatchThreshold=threshold,
                                              MaxFaces=maxFaces)
        faceMatches=response['FaceMatches']
        print ('Matching faces')
        for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('External Id:' + match['Face']["ExternalImageId"])
            print ('Similarity:' + "{:.2f}".format(match['Similarity']) + "%")
            
if __name__=="__main__":
    main()
    
