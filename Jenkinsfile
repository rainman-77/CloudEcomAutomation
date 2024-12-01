pipeline {
    agent any

    environment {
        REPORT_DIR = 'reports'            // JSON reports folder in the project
        ALLURE_REPORT_DIR = 'allure_report' // Final Allure HTML report folder in the project
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install required packages and dependencies
                sh '''
                sudo yum update -y
		        sudo yum install python3 -y
                sudo yum install python3-pip -y
                sudo yum install docker -y

                # Start Docker service only if not already running
                if ! sudo systemctl is-active --quiet docker; then
                    sudo systemctl start docker
                fi

                # Enable Docker to start on boot only if not already enabled
                if ! sudo systemctl is-enabled --quiet docker; then
                    sudo systemctl enable docker
                fi

                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Set Up Selenium Grid') {
            steps {
                // Start Selenium Grid using Docker Compose
                    sh '''
                    docker-compose up -d
		            echo "Waiting for Selenium Grid Hub to be available..."
        	        for i in {1..15}; do
                     if curl -s http://localhost:4444/status | grep -q '"ready":true'; then
                      echo "Selenium Grid Hub is ready."
                      break
                     fi
                     echo "Waiting for Selenium Grid Hub to initialize..."
                     sleep 2
                    done
                    '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Pytest and save Allure JSON reports to the "reports" folder
                    sh '''
                    pytest --alluredir=${REPORT_DIR} -n 3
                    '''
            }
        }
    }
    post {
            always {
                echo 'Always execute post-actions, even if the stage fails.'
                // Generate Allure HTML report in the "allure_report" folder
                sh '''
                allure generate ${REPORT_DIR} --clean -o ${ALLURE_REPORT_DIR}
                '''
                // Add post-build step to display Allure report in Jenkins
                // Archive Allure report
                allure([
                    results: [[path: "${REPORT_DIR}"]],
                    reportBuildPolicy: 'ALWAYS'
                ])
                // Tear down Selenium Grid
                sh '''
		        docker-compose down
		        '''
            }
     }
}