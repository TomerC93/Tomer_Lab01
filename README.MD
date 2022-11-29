Final K8S Project Jhon Bryce - by Tomer Cohen

Project installation + explenation:

1. app.py - Python application ready to build
2. Dockerfile - docker file to build python app
3. Jenkinsfile - Jenkins file ready that builds the app from the docker file, tests it, updating K8S values.yaml build version, tag it, push it to the docker hub and generate commit+PR on GitHub.
4. argocd folder - all the project files that builds and run the HELM chart in k8s.
5. kube folder - HELM chart for the application that builds the app from the image on K8S.