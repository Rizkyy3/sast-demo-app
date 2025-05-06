pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rizkyy3/sast-demo-app.git', branch: 'master'
            }
        }

<<<<<<< HEAD
=======
        stage('Install Bandit') {
            steps {
                // Menambahkan pip3 ke PATH untuk memastikan pip3 tersedia
                sh 'export PATH=$PATH:/usr/local/bin && pip3 install bandit'
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
HEAD
pipeline {
    agent any  // Menjalankan pipeline di mesin mana saja yang tersedia

    stages {
        stage('Checkout') {
            steps {
                // Mengambil kode dari repositori GitHub
                git url: 'https://github.com/username/sast-demo-app.git', branch: 'master'
            }
        }
>>>>>>> aa5d3c9 (Fix pip path in Jenkinsfile)
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
