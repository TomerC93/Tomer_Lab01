pipeline {
    agent any
    
    parameters {
        string defaultValue: '500', name: 'INTERVAL'
        string defaultValue: 'AKIA3LTSIWSZXTJUUYWF', name: 'ID'
        string defaultValue: 'B0BX2jw7jnZ+Rpglh9X3osba2EJIOwa+1m7WQfXe', name: 'ACCESS'
        string defaultValue: 'tomercohen1993', name: 'USERNAME'
        string defaultValue: 'Tomer12341234!', name: 'PASSWORD'
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
               git branch: 'develop', url: 'https://github.com/TomerC93/Tomer_Lab01.git'
            }
        }
        
         stage('Install YQ') {
            steps {
               sh 'apt install wget && wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && chmod +x /usr/bin/yq'
            }
        }
        
          stage('Install GH git') {
            steps {
               sh '''
                apt update
                apt install gh -y
               '''
            }
        }
        
         stage('Update Version') {
            steps {
               sh """
               pwd
               yq -i \'.image.tag = \"${BUILD_NUMBER}\"\' kube/values.yaml
               """
            }
        }

        stage('Build and Test') {
            steps {
                sh 'docker build -t tomercohen1993/production:1.1${BUILD_NUMBER} .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag tomercohen1993/production:1.1${BUILD_NUMBER} tomercohen1993/production:1.1${BUILD_NUMBER}'
            }
        }

        stage('Docker Login') {
            steps {
                sh 'docker login -u ${USERNAME} -p ${PASSWORD} '
            }
        }
        
        
        stage('Push Image') {
            steps {
                sh 'docker push tomercohen1993/production:1.1${BUILD_NUMBER}'
            }
        }
        
          stage('Git Commit') {
            steps {
                sh '''
                git config --global user.email tomer123321@gmail.com
                git config --global user.name TomerC93
                git add .
                git commit -m "Build number ${BUILD_NUMBER} commited"
                git push https://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@github.com/TomerC93/Tomer_Lab01.git --all
                '''
            }
        }
        
         stage('Git PR') {
            steps {
                sh '''
                gh auth login --with-token < token.txt
                gh pr create --base master --head develop -m "Pr from develop"
                '''
            }
        }
     }
}