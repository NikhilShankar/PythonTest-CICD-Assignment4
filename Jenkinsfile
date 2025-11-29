pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application on localhost:9876...'
                bat '''
                    taskkill /F /IM python.exe /FI "WINDOWTITLE eq *app.py*" 2>nul || echo No previous instance
                    start /B python app.py
                '''
                echo "Deployment completed at: ${new Date()}"
            }
        }
    }
}
