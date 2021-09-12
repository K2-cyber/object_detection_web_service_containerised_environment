from flask import Flask, redirect, url_for, request, jsonify
import sys
import json
import base64
from random import randrange

sys.path.append("/usr/src/app/object_detection")
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    i = 1
    return 'welcome %s' % name


@app.route('/object_json', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        image_json_request = request.get_json()
        image_json = json.loads(image_json_request)
        with open('data.json', 'w') as f:
            json.dump(a, f)
        img_data = image_json["image"]
        id = image_json['id']
        random_int = randrange(31)
        import object_detection as detection_code
        print("Saving in " + "/usr/src/app/imageToSave" + str(random_int) + ".jpg")
        with open("/usr/src/app/imageToSave" + str(random_int) + ".jpg", "wb") as fh:
            fh.write(base64.b64decode(img_data))

            object_response = detection_code.main("/usr/src/app/yolo_tiny_configs",
                                                  "/usr/src/app/imageToSave" + str(random_int) + ".jpg")


        finalResonse = {}
        allObjects = []
        finalResonse['id'] = id
        for each_response in object_response:
            objects = {}
            rectangle = {}
            objects['label'] = each_response[0]
            objects['accuracy'] = each_response[1]
            rectangle['height'] = each_response[2]
            rectangle['left'] = each_response[3]
            rectangle['top'] = each_response[4]
            rectangle['width'] = each_response[5]
            objects['rectangle'] = rectangle
            allObjects.append(objects)
        finalResonse['objects'] = allObjects

        return jsonify(json.dumps(finalResonse))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    print("Starting the server")
    try:

        app.run(debug=True, threaded=True, host="0.0.0.0")

    except Exception as e:

        print("Exception occured")
        print(e)
