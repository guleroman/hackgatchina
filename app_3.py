from flask import Flask, jsonify, request, json, make_response
import uuid, time,os
import requests

# python OCR_snils.py --image=snils_data/image1.jpg

import numpy as np
import tensorflow as tf
from PIL import Image
from utils import label_map_util
from utils import visualization_utils as vis_util
import cv2
import matplotlib.pyplot as plt
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


PATH_TO_CKPT = 'trainedModels/ssd_mobilenet_RoadDamageDetector.pb' # Путь к обученной модели нейросети
PATH_TO_LABELS = 'trainedModels/crack_label_map.pbtxt'  # Путь к label-файлу
NUM_CLASSES = 8
IMAGE_SIZE = (12, 8)
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

@app.route('/api/<file_name>',methods=['GET'])
def write_image(file_name):      
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            IMAGE_PATH = '/home/ml/RoadDamageDetector/33/'+file_name
            sess.run(tf.global_variables_initializer())
            image = Image.open(IMAGE_PATH)
            (im_width, im_height) = image.size 
            image_np = np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)
            to_pixel = np.array([im_height, im_width, im_height, im_width])
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            (boxes, scores, classes, num_detections) = sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})  
            vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            min_score_thresh=0.3,
            use_normalized_coordinates=True,
            line_thickness=8)
            plt.figure(figsize=IMAGE_SIZE)
            plt.savefig('new'+file_name)
    return jsonify('ok')

if __name__ == '__main__':

    app.run(debug=False,threaded = True, host='0.0.0.0', port=6060)


#ip = 'http://80.78.255.16:6060'

#def get_output_file(name):
#    try:
#        return send_file(name, as_attachment=True)
#    except:
#        return make_response(jsonify({"_status_code":404,"error":{"document":"file is not ready yet"}}),404)

#def say_hi():#176.99.11.61
#    link = ip + '/api/companies/'+provider_inn+'/documents'
#    header = {'key':key} 
#    try:
#        requests.post(link, data = json.dumps(existing_fields,ensure_ascii=True), headers = header, timeout=0.0001)
#    except:
#        print ("Выполнил - "+key)



#@app.route('/api',methods=['POST'])
#def resp(id):
#    with open(new_file, mode="wb") as new:
#        new.write(response.content)
#    message = {"_status_code":200,"error":{}}
#    #start_time = time.time()
#    #provider_inn = str(prov_inn)
#    key = str(uuid.uuid4())
#    try:
#        data_post = json.loads(request.data)
#    except:
#        message['error'].update({"info":"incorrect POST-request"})
#        message.update({"_status_code":422})


