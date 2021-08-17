import boto3
import csv
        
client = boto3.client('rekognition',
                      aws_access_key_id ="AKIAVSOODXZIA2N63CAP",
                      aws_secret_access_key ="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",
                      region_name ='us-east-1'
                        )

def create_collection(collection_id):
    
    print('Creating collection:' + collection_id)
    
    response=client.create_collection(CollectionId=collection_id)
    
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main():
    collection_id='Intelligent_Album_ManageRR'
    create_collection(collection_id)
    
if __name__=="__main__":
    main()