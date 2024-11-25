pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'  // Create virtual environment
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh '. venv/bin/activate && python3 -m unittest discover -s tests -p "test_*.py" > result.xml'
                    } catch (Exception e) {
                        echo 'Tests failed'
                    }
                }
            }
        }

        stage('Email Results') {
            steps {
                script {
                    def testResult = junit '**/result.xml'
                    def emailBody = """
                    Test Report:
                    Total Tests: ${testResult.totalCount}
                    Passed: ${testResult.passedCount}
                    Failed: ${testResult.failedCount}
                    Skipped: ${testResult.skippedCount}
                    """

                    emailext (
                        subject: "Daily Test Results",
                        body: emailBody,
                        to: "your-email@example.com"
                    )
                }
            }
        }
    }
}
