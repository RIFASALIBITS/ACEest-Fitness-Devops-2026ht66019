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
                sh 'python3 -m pip install -r requirements.txt -r requirements-dev.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'python3 -m flake8 app.py tests/'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build --target test -t aceest-fitness:test .'
                sh 'docker run --rm aceest-fitness:test'
            }
        }
    }
}
