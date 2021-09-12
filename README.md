# object_detection_web_service_containerised_environment

This project aims at building a web-based system that we call it iWebLens.
It allows end-users to send an image to a web service hosted in a Docker container and receive a list of objects detected in their uploaded image. The project makes use of YOLO (You only look once) library, a state-of-the-art real-time object detection system, and OpenCV (Open-Source Computer Vision Library) to perform required image operations/transformations.
Both YOLO and OpenCV are python-based open-source computer vision and machine learning software libraries.
The web service will be hosted as container in a Kubernetes cluster. Kubernetes is used as the container orchestration system. The object detection web service is also de- signed to be a RESTful API that can use Python’s FLASK library.
We are interested in examining the performance of iWebLens by varying the rate of requests sent to the system (demand) and the number of existing Pods within the Kubernetes cluster (resources).

These are the following objectives:

• Writing a python web service that accepts images in JSON object format, uses YOLO and OpenCV to process images, and returns a JSON object with a list of detected objects.
• Building a Docker Image for the object detection web service.
• Creating a Kubernetes cluster on a virtual machine (instance) in the Nectar cloud.
• Deploying a Kubernetes service to distribute inbound requests among pods that are running the object detection service.
• Testing the system under different load and number of pods.
