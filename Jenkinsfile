pipeline {
    agent any

    environment {
        PYTHON = 'python' // Adjust if needed
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vengadeswar/SauceDemoAutomation.git', credentialsId: 'github'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest with rerun for failed tests (2 retries, 5s delay)
                bat 'pytest -v -s --reruns 2 --reruns-delay 5 --alluredir=Reports/allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate Reports/allure-results -o Reports/allure-report --clean'
            }
        }

        stage('Open Allure Report') {
            steps {
                bat 'allure open Reports/allure-report'
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
