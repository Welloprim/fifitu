import requests, json
import http.client, urllib.parse
import json
import os.path
from azure.cognitiveservices.search.visualsearch import VisualSearchClient
from azure.cognitiveservices.search.visualsearch.models import (
    VisualSearchRequest,
    CropArea,
    ImageInfo,
    Filters,
    KnowledgeRequest,
)
from msrest.authentication import CognitiveServicesCredentials

subscription_key = '9cd2655c2ff34fd2b28cbd330b583140'
PATH = 'C:\\Users\\USER\\azure-cognitive-samples\\mytestenv\\TestImages\\'
image_path2 = os.path.join(PATH, "image.jpg")
image_path = "jean_test.jpeg"

client = VisualSearchClient(endpoint="https://api.cognitive.microsoft.com",
                            credentials=CognitiveServicesCredentials(subscription_key))

with open(image_path, "rb") as image_fd:
    # You need to pass the serialized form of the model
    knowledge_request = json.dumps(VisualSearchRequest().serialize())

    print("\r\nSearch visual search request with binary of dog image")
    result = client.images.visual_search(image=image_fd, knowledge_request=knowledge_request)

if not result:
    print("No visual search result data.")

    # Visual Search results
if result.image.image_insights_token:
    print("Uploaded image insights token: {}".format(result.image.image_insights_token))
else:
    print("Couldn't find image insights token!")

    # List of tags
if result.tags:
    first_tag = result.tags[0]
    print("Visual search tag count: {}".format(len(result.tags)))

    # List of actions in first tag
    if first_tag.actions:
        first_tag_action = first_tag.actions[0]
        print("First tag action count: {}".format(len(first_tag.actions)))
        print("First tag action type: {}".format(first_tag_action.action_type))
    else:
        print("Couldn't find tag actions!")
else:
    print("Couldn't find image tags!")