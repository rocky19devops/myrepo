pipeline {
    agent any
      environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
                HOME = "${env.WORKSPACE}"
      }
    stages {
        stage('Checkout') {
            steps {
                echo "Hello Rocky World ${BUILD_NUMBER}"
                git branch: 'main', url: 'https://github.com/rocky19devops/myrepo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Docker Image..............'
                sh "docker build -t rocky19devops/myrepo:${BUILD_NUMBER} ."
                }
        }
        
        stage('Push Code') {
            steps {
                // withCredentials([usernamePassword(credentialsId: 'rockydockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                withCredentials([ credentialsId: 'dockerHubUser' ]) {
                echo 'Pushing image to Docker Repository..............'
                sh "docker push rocky19devops/myrepo:${BUILD_NUMBER}"
                }
            }
        }

        stage('Run') {
            steps {
                echo 'Run the docker application............'
                sh "docker run --name rockyapp${BUILD_NUMBER} rocky19devops/myrepo:${BUILD_NUMBER}"
            }
        }
    }
}

