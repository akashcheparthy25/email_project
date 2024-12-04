pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/akashcheparthy25/email_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    pytest tests/ --maxfail=5 --disable-warnings --tb=short --junitxml=result.xml | tee result.log
                    '''
                }
            }
        }
    }

    post {
        always {
            junit '**/result.xml'  // Jenkins will parse the result.xml and trigger actions based on test results
        }

        failure {
            mail to: 'cheparthyakash0925@gmail.com',
                 subject: "Build Failed: ${currentBuild.fullDisplayName}",
                 body: "The build has failed. Please check the Jenkins console output for details."
        }
    }
}
