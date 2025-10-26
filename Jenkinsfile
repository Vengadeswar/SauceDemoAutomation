pipeline {
    agent any

    environment {
        PYTHON = "C:\\Python312\\python.exe"
        PIP = "C:\\Python312\\Scripts\\pip.exe"
        ALLURE = "C:\\allure\\bin\\allure.bat"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Vengadeswar/SauceDemoAutomation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "${PIP} install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${PYTHON} -m pytest -v -s --alluredir=Reports/allure-results"
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    if (fileExists("${ALLURE}")) {
                        bat "${ALLURE} generate Reports/allure-results -o Reports/allure-report --clean"
                    } else {
                        echo "Allure not found, skipping report generation"
                    }
                }
            }
        }

        stage('Archive Allure Report') {
            steps {
                archiveArtifacts artifacts: 'Reports/allure-report/**', allowEmptyArchive: true
            }
        }

    }

    post {
        always {
            cleanWs()
        }
    }
}
