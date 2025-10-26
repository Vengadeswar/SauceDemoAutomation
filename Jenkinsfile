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
                echo "Checking out code from GitHub..."
                git credentialsId: 'github', url: 'https://github.com/Vengadeswar/SauceDemoAutomation.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                bat """
                if exist "${PIP}" (
                    ${PIP} install --upgrade pip
                    ${PIP} install -r requirements.txt
                ) else (
                    echo Pip not found at ${PIP}
                    exit 1
                )
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running Pytest automation..."
                bat """
                if exist "${PYTHON}" (
                    ${PYTHON} -m pytest -v -s --alluredir=Reports/allure-results
                ) else (
                    echo Python not found at ${PYTHON}
                    exit 1
                )
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure Report..."
                bat """
                if exist "${ALLURE}" (
                    ${ALLURE} generate Reports/allure-results -o Reports/allure-report --clean
                ) else (
                    echo Allure not found at ${ALLURE}, skipping report generation
                )
                """
            }
        }

        stage('Archive Allure Report') {
            steps {
                echo "Archiving Allure Report..."
                archiveArtifacts artifacts: 'Reports/allure-report/**', allowEmptyArchive: true
            }
        }

    }

    post {
        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
    }
}
