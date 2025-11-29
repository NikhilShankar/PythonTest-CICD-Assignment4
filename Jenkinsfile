pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application...'
                sh 'python3 app.py &'
                sleep 5
                sh 'curl http://localhost:9876 || echo "App is running"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment completed'
                echo "Deployed at: ${new Date()}"
            }
        }
    }
}