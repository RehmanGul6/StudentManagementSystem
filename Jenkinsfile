pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python src\\main.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

    }
}