#import dependencies
from google.cloud import vision
from google.cloud import storage
from google.cloud.vision_v1 import enums
from google.cloud.vision_v1 import ImageAnnotatorClient
from google.cloud.vision_v1 import types
import os
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='project_key.json' 
#(created in step 1)
# Get GCS bucket
storage_client = storage.Client()
bucket = storage_client.bucket('bucket_name')
image_paths = []
for blob in list(bucket.list_blobs()):
    image_paths.append("gs:// bucket_name/"+blob.name)
# We can send a maximum of 16 images per request.
start = 0
end = 16
label_output = []
for i in range(int(np.floor(len(image_paths)/16))+1):
    requests = []
    client = vision.ImageAnnotatorClient()
    for image_path in image_paths[start:end]:
        image = types.Image()
        image.source.image_uri = image_path
        requests.append({'image': image,'features': [{'type': enums.Feature.Type.LABEL_DETECTION}]})
        response = client.batch_annotate_images(requests)
    for image_path, i in zip(image_paths[start:end], response.responses):
        labels = [{label.description: label.score} for label in i.label_annotations]
        labels = {k: v for d in labels for k, v in d.items()}
        filename = os.path.basename(image_path)
        l = {'filename': filename, 'labels': labels}
        label_output.append(l)
    start = start+16
    end = end+16
#export results to JSON file
with open('image_results.json', 'w') as outputjson:
json.dump(label_output, outputjson, ensure_ascii=False)