pipeline {
    agent any
    parameters {
        string defaultValue: '500', name: 'INTERVAL'
    }
    environment {
        CRED = credentials('credentials')
        CONFIG = credentials('config')
    }

    stages {
        stage('CleanWs') {
            steps {
                cleanWs()
            }
        }
        stage('RemoveRunningContainer') {
            steps {
                sh "docker stop myapp:${oldBuild}=={${currentBuild.number}-1 } "
                sh "docker rm myapp:${oldBuild}=={${currentBuild.number}-1 }"
                sh "docker rmi myapp:${oldBuild}=={${currentBuild.number}-1 }"
            }
        }
        stage('GetSCM') {
            steps {
                git url: 'https://github.com/TomerC93/Tomer_Lab01.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                print currentBuild.number
                sh "cat $CRED | tee credentials"
                sh "cat $CONFIG | tee config"
                sh "docker build -t myapp:${currentBuild.number} ."
            }
        }
        stage('Deploy') {
            steps {
                sh "docker run -itd --name myapp:${currentBuild.number} --env INTERVAL=${params.INTERVAL} myapp"
            }
        stage('Login') {
            steps {
                sh "docker login -u 'Tomer USERNAME EXAMPLE' -p -'Tomer PASSWORD Example' "
            }
        }
        stage('Push') {
            steps {
                sh "docker push myapp:${currentBuild.number}"
            }
        }
        stage('Logout') {
            steps {
                sh "docker logout"
            }
        }
    }
}

