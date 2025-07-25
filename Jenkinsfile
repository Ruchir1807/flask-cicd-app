pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "📥 Cloning repo..."
                sh 'rm -rf flask-cicd-app'
                sh 'git clone https://github.com/Ruchir1807/flask-cicd-app.git'
                dir('flask-cicd-app') {
                    sh 'ls -l'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('flask-cicd-app') {
                    echo "📦 Building Docker image..."
                    sh 'docker build -t flask-k8s-app .'
                }
            }
        }

        stage('Load Image into Minikube') {
            steps {
                echo "📤 Loading image into Minikube..."
                timeout(time: 2, unit: 'MINUTES') {
                    sh 'minikube image load flask-k8s-app'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "🚀 Deploying to Kubernetes..."
                timeout(time: 2, unit: 'MINUTES') {
                    sh '''
                        kubectl apply -f flask-cicd-app/deployment.yaml --validate=true
                        kubectl apply -f flask-cicd-app/service.yaml --validate=true
                    '''
                }
            }
        }

        stage('Debug Info') {
            steps {
                echo "🔍 Getting pod status and logs..."
                sh 'sleep 10'
                script {
                    def podName = sh(
                        script: 'kubectl get pods -o jsonpath="{.items[0].metadata.name}"',
                        returnStdout: true
                    ).trim()

                    echo "📄 Pod Name: ${podName}"

                    sh "kubectl describe pod ${podName} || true"
                    sh "kubectl logs ${podName} || true"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully."
        }
        failure {
            echo "❌ Pipeline failed. Please check the logs above for details."
        }
    }
}
