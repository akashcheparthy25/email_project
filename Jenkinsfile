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
                    // Verify if requirements.txt exists before attempting installation
                    sh '''
                    if [ -f requirements.txt ]; then
                        python3 -m venv venv
                        ./venv/bin/pip install --upgrade pip
                        ./venv/bin/pip install -r requirements.txt
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
                    // Run the tests with pytest
                    sh './venv/bin/pytest tests/'
                }
            }
        }
    }
}
