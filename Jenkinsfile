pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/akashcheparthy25/email_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure requirements.txt exists before continuing
                    sh '''
                    if [ -f requirements.txt ]; then
                        # Create virtual environment if it doesn't exist
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi

                        # Activate virtual environment and install dependencies
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    else
                        echo "requirements.txt not found"
                        exit 1
                    fi
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests with pytest and save the result to a file
                    sh '''
                    . venv/bin/activate
                    pytest tests/ --maxfail=5 --disable-warnings --tb=short > result.log || true
                    '''
                }
            }
        }

        stage('Post-build Actions') {
            steps {
                script {
                    // Parse the result.log file to check if there are any failed tests
                    def failedTests = sh(script: 'grep "E       " result.log || true', returnStdout: true).trim()

                    if (failedTests) {
                        // Send an email if there are failed tests
                        emailext (
                            subject: "Test Failures Detected in Jenkins Build #${currentBuild.number}",
                            body: "The following tests failed:\n\n${failedTests}\n\nPlease review the build logs for more details.",
                            to: "cheparthy.akash@smithsdetection.com"
                        )
                    }
                }
            }
        }
    }
}
