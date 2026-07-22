pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\rehma\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\rehma\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" src\\main.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\rehma\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pytest'
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