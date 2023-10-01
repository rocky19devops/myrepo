pipeline {
  agent {
    docker {
      image 'docker:latest'
      args '--user root -v /var/run/docker.sock:/var/run/docker.sock' // mount Docker socket to access the host's Docker daemon
    }
  }
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
          environment {
            DOCKER_IMAGE = "rocky19devops/myrepo:${BUILD_NUMBER}"
            REGISTRY_CREDENTIALS = credentials('rockydockerhub')
          }
            steps {
              script {
                def dockerImage = docker.image("${DOCKER_IMAGE}")
                docker.withRegistry('https://index.docker.io/v1/', "rockydockerhub") {
                dockerImage.push()
                }
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

