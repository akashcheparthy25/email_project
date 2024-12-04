pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3' // Adjust if your Python version is different
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/username/project_email.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install --upgrade pip'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run all test scripts and output results
                    sh './venv/bin/pytest tests/'
                }
            }
        }
    }
}
