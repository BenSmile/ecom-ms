pipeline {
    agent {
        label "jenkins-agent"
    }

    tools{
        jdk 'Java17'
        maven 'Maven3'
    }

    stages{
         stage("Cleanup Workspace") {
            steps {
                cleanWs()
            }
         }
         stage("Checkout from SCM") {
            steps {
                git branch: 'dev', credentialsId: 'github_credentials', url: 'https://github.com/BenSmile/ecom-ms'
            }
         }
    }
}