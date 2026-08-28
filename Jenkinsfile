pipeline {
    agent any

    environment {
        IMAGE = "souley123/velos-api"
        TAG   = "${env.BUILD_NUMBER}"
    }

    options {
        timeout(time: 20, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Tester') {
            steps {
                sh 'docker build --target test -t velos-api:test-$TAG .'
            }
        }
        stage('Construire') {
            steps {
                sh 'docker build -t $IMAGE:$TAG -t $IMAGE:latest .'
            }
        }
        stage('Publier') {
            steps {
                withCredentials([usernamePassword(
                        credentialsId: 'docker-hub',
                        usernameVariable: 'REGISTRE_USER',
                        passwordVariable: 'REGISTRE_PASS')]) {
                    sh '''
                        echo "$REGISTRE_PASS" | docker login -u "$REGISTRE_USER" --password-stdin
                        docker push $IMAGE:$TAG
                        docker push $IMAGE:latest
                    '''
                }
            }
        }
        stage('Deployer') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-velos', variable: 'KUBECONFIG')]) {
                    sh '''
                        kubectl set image deployment/velos-api api=$IMAGE:$TAG
                        kubectl rollout status deployment/velos-api --timeout=180s
                    '''
                }
            }
        }
    }
}
