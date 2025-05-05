pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Bandit') {
            steps {
                sh 'pip install bandit'
            }
        }

        stage('Run Bandit') {
            steps {
                sh 'bandit -r . || true'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Bandit') {
            steps {
                sh 'pip install bandit'
            }
        }

        stage('Run Bandit') {
            steps {
                sh 'bandit -r . || true'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Bandit') {
            steps {
                sh 'pip install bandit'
            }
        }

        stage('Run Bandit') {
            steps {
                sh 'bandit -r . || true'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Bandit') {
            steps {
                sh 'pip install bandit'
            }
        }

        stage('Run Bandit') {
            steps {
                sh 'bandit -r . || true'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Bandit') {
            steps {
                sh 'pip install bandit'
            }
        }

        stage('Run Bandit') {
            steps {
                sh 'bandit -r . || true'
            }
        }
    }
}
<<<<<<< HEAD
pipeline {
    agent any  // Menjalankan pipeline di mesin mana saja yang tersedia

    stages {
        stage('Checkout') {
            steps {
                // Mengambil kode dari repositori GitHub
                git url: 'https://github.com/username/sast-demo-app.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Menginstal Bandit
                sh 'pip install bandit'
            }
        }
        stage('SAST Analysis') {
            steps {
                // Menjalankan Bandit dan menghasilkan output XML
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                // Menyimpan hasil analisis di Jenkins
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
=======
>>>>>>> 056208d (Add Jenkinsfile for SAST pipeline)

