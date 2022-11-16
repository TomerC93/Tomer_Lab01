pipeline {
    agent any
    
    parameters {
        string defaultValue: '500', name: 'INTERVAL'
        string defaultValue: 'None', name: 'ID'
        string defaultValue: 'None', name: 'ACCESS'
        string defaultValue: 'None', name: 'USERNAME'
        string defaultValue: 'None', name: 'PASSWORD'
    }
    
    
    stages {
        
        
        stage('CREATE ENV') {
            steps {
               sh "echo KEY_ID=$ID >> .env"
               sh "echo ACCESS_KEY=$ACCESS >> .env"
            }
        }
    
        stage('GET SCM') {
            steps {
               git branch: 'main', url: 'https://github.com/TomerC93/Tomer_Lab01.git'
            }
        }

        stage('Build and Test') {
            steps {
                sh 'docker build -t tomercohen1993/production:1.1.${BUILD_NUMBER} .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag tomercohen1993/production:1.1.${BUILD_NUMBER} tomercohen1993/production:1.1.${BUILD_NUMBER}'
            }
        }

        stage('Docker Login') {
            steps {
                sh 'docker login -u ${USERNAME} -p ${PASSWORD} '
            }
        }
        
        
        stage('Push Image') {
            steps {
                sh 'docker push tomercohen1993/production:1.1.${BUILD_NUMBER}.${BUILD_NUMBER}'
            }
        }
     }
}