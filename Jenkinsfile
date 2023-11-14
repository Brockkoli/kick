pipeline {
    agent any
    environment {
        PATH = "/usr/bin:$PATH"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                git 'http://172.17.0.1:3000/repository.git'
            }
        }

        stage('OWASP DependencyCheck') {
            steps {
                dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP test'
            }
        }

        stage('UI Tests') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'sudo apt-get install -y python3-flask'
                    sh 'python3 test_ui.py'
                }
            }
        } 

        stage('Code Quality Check via SonarQube') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                        def scannerHome = tool 'SonarQube';
                        withSonarQubeEnv('SonarQube') {
                            sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=$SONAR_TOKEN -Dsonar.projectKey=practice -Dsonar.sources=."
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
        failure {
            echo "The build failed."
        }
    }
}
