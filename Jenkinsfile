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
                    // Run all test scripts
                    sh './venv/bin/pytest tests/ --junitxml=test-results.xml'
                }
            }
        }
    }

    post {
        always {
            // Archive test results
            archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true

            // Optional: Send email notification
            mail to: 'your-email@example.com',
                 subject: "Test Results for Build #${env.BUILD_NUMBER}",
                 body: "The test run is complete. Please check the test results in Jenkins."
        }
    }
}
