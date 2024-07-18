pipeline {
    agent {
        label 'jenkins-agent'
    }

    tools {
        jdk 'Java17'
        maven 'Maven3'
    }

    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout from SCM') {
            steps {
                git branch: 'dev', credentialsId: 'github_credentials', url: 'https://github.com/BenSmile/ecom-ms'
            }
        }

        stage('Build Application') {
            steps {
                sh 'mvn clean package -DskipTests=true'
            }
        }

        stage('Build Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Sonarqube Analysis') {
            steps {
                withSonarQubeEnv(credentialsId: 'jenkins_sonarqube_token') {
                    sh 'mvn sonar:sonar'
                }
            }
        }
    }
}
