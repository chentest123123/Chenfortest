pipeline {

  environment {
    dockerimagename = "chenlulu/python-app"
    dockerImage = ""
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git 'https://github.com/chentest123123/Chenfortest.git'
      }
    }

    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
        }
      }
    }

    stage('Pushing Image') {
      environment {
               registryCredential = 'gitlab-credentials'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.gitlab.com', registryCredential ) {
            dockerImage.push("1.0.0v")
          }
        }
      }
    }

    stage('Deploying React.js container to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", "service.yaml")
        }
      }
    }
  }
}
