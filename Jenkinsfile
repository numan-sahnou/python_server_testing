pipeline {
    agent any

    stages {
        stage('NPM Build') {
            steps{
                bat 'npm install'
                bat 'npm start'
            }
        }
    }
}