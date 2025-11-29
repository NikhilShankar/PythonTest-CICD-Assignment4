pipeline {

    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'ref', value: '$.ref']
            ],
            causeString: 'Triggered by Gitea',
            token: 'my-secret-gitea-token-123',  // <-- This is YOUR_TOKEN
            printContributedVariables: true,
            printPostContent: true
        )
    }

    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
                sh 'ls -la'
            }
        }

        stage('Validate') {
            steps {
                echo 'Validating project structure...'
                sh '''
                    echo "Checking for required files..."
                    test -f app.py && echo "✓ app.py found" || echo "✗ app.py missing"
                    test -f requirements.txt && echo "✓ requirements.txt found" || echo "✗ requirements.txt missing"
                    test -f Jenkinsfile && echo "✓ Jenkinsfile found" || echo "✗ Jenkinsfile missing"
                '''
            }
        }

        stage('Build Info') {
            steps {
                echo 'Displaying build information...'
                sh '''
                    echo "Repository: PythonTest-CICD-Assignment4"
                    echo "Branch: ${GIT_BRANCH}"
                    echo "Commit: ${GIT_COMMIT}"
                    cat app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '✓ Pipeline completed successfully!'
                echo "Build finished at: ${new Date()}"
            }
        }
    }
    
    post {
        success {
            echo '✓ Build SUCCESS - All stages passed!'
        }
        failure {
            echo '✗ Build FAILED'
        }
    }
}