pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Pastikan pip terinstal sebelum menjalankan Bandit
                sh 'python3 -m ensurepip --upgrade'  // Menginstal pip jika belum terpasang
                sh 'pip3 install bandit'  // Instal Bandit dengan pip3
            }
        }

        stage('SAST Analysis') {
            steps {
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
