pipeline {
    agent any

    environment {
        // Ensure Jenkins uses the correct KUBECONFIG path
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning GitHub repository..."
                git branch: 'main', url: 'https://github.com/Ruchir1807/flask-cicd-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t flask-k8s-app .'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                echo "Loading image into Minikube..."
                timeout(time: 2, unit: 'MINUTES') {
                    sh 'minikube image load flask-k8s-app'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes using KUBECONFIG at $KUBECONFIG..."
                timeout(time: 2, unit: 'MINUTES') {
                    sh '''
                        kubectl apply -f deployment.yaml --validate=true
                        kubectl apply -f service.yaml --validate=true
                    '''
                }
            }
        }

        stage('Debug Info') {
            steps {
                echo 'Getting pod status and logs for debug...'
                // Add a small wait to give time for pod creation
                sh 'sleep 10'
                sh 'kubectl get pods -o wide'
                sh 'kubectl describe pod $(kubectl get pods -o jsonpath="{.items[0].metadata.name}") || true'
                sh 'kubectl logs $(kubectl get pods -o jsonpath="{.items[0].metadata.name}") || true'
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
