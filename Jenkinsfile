pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config'  // Ensure this file is readable by Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "🔄 Cloning repository..."
                git branch: 'main', url: 'https://github.com/Ruchir1807/flask-cicd-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "📦 Building Docker image..."
                sh 'docker build -t flask-k8s-app .'
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
                        kubectl apply -f k8s/deployment.yaml --validate=true
                        kubectl apply -f k8s/service.yaml --validate=true
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
