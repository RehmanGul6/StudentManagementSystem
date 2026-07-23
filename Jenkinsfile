pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat 'py src\\main.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'py -m pytest'
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Please check the console output.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}