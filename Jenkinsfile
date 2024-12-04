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
                    sh '''
                    if [ -f requirements.txt ]; then
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi
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
                    // Check if there are failed tests in result.log
                    def failedTests = sh(script: 'grep "E       " result.log || true', returnStdout: true).trim()

                    // Debugging: Print the result of the failure check
                    echo "Failed Tests Found: ${failedTests}"

                    if (failedTests) {
                        // Send email if failed tests exist
                        emailext (
                            subject: "Test Failures Detected in Jenkins Build #${currentBuild.number}",
                            body: "The following tests failed:\n\n${failedTests}\n\nPlease review the build logs for more details.",
                            to: "cheparthyakash0925@.com"
                        )
                    } else {
                        echo "No failed tests found"
                    }
                }
            }
        }
    }
}
