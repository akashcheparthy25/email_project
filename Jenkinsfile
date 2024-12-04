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
                    // Run the tests with pytest
                    sh './venv/bin/pytest tests/'
                }
            }
        }
    }
}
