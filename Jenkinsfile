pipeline {
    agent any

    stages {


        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Stop old container') {
            steps {
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run new container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }
}