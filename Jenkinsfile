pipeline {
    agent any

    environment {
        // Correct path to Minikube config copied into Jenkins
        KUBECONFIG = '/var/lib/jenkins/.minikube/profiles/minikube/config'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Ruchir1807/flask-cicd-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-k8s-app .'
            }
        }

        stage('Load into Minikube') {
            steps {
                sh 'minikube image load flask-k8s-app'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    echo "Using KUBECONFIG at: $KUBECONFIG"
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                '''
            }
        }
    }
}
