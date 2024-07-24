pipeline {
    agent {
        label 'jenkins-agent'
    }

    tools {
        jdk 'Java17'
        maven 'Maven3'
    }

    environment {
        APP_NAME = 'complete-production-e2e'
        RELEASE = '1.0.0'
        DOCKER_USERNAME = 'benkafirongo'
        DOCKER_PASSWORD = 'dockerhub'
        IMAGE_NAME = "${DOCKER_USERNAME}" + '/' + "${APP_NAME}"
        IMAGE_TAG = "${RELEASE}-${env.BUILD_NUMBER}"
        JENKINS_API_TOKEN = "${JENKINS_API_TOKEN}"
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
                script {
                    withSonarQubeEnv(credentialsId: 'jenkins_sonarqube_token') {
                        sh 'mvn sonar:sonar'
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    waitForQualityGate abortPipeline: false, credentialsId: 'jenkins_sonarqube_token'
                }
            }
        }

        stage('Build and Push Docker image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_PASSWORD) {
                        docker_image = docker.build "${IMAGE_NAME}"
                    }

                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_PASSWORD) {
                        docker_image.push("${IMAGE_TAG}")
                        docker_image.push('latest')
                    }
                }
            }
        }

        stage('Trigger CD pipeline') {
            steps {
                script {
                    sh "curl -v -k --user admin:${JENKINS_API_TOKEN} -X POST -H 'cache-control: no-cache' -H 'content-type: application/x-www-form-urlencoded' --data 'IMAGE_TAG=${IMAGE_TAG}' 'https://jenkins.bkafirongo.com/job/gitops-ecom-pipeline/buildWithParameters?token=gitops_ecom_token'"
                }
            }
        }
    }
}
