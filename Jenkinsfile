pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application...'
                sh 'python --version'
                sh 'python -c "from flask import Flask; print(\'Flask imported successfully\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage'
                echo "Build completed at: ${new Date()}"
            }
        }
    }
}