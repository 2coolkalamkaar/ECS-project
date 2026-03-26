pipeline {
    agent any
    
    // Environment variables tailored to your AWS setup
    environment {
        AWS_REGION     = 'us-east-1'
        AWS_ACCOUNT_ID = '851079560395'
        ECR_REPO       = 'demorepo'
        ECR_URI        = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"
        
        // Your specific ECS target
        ECS_CLUSTER    = 'demo-cluster' 
        ECS_SERVICE    = 'demo-cluster_td-service-u615hyal' 
        
        // Tagging with Jenkins Build Number for strict version control
        IMAGE_TAG      = "v_${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo " Building Image..."
                    sh "docker build -t ${ECR_URI}:${IMAGE_TAG} -t ${ECR_URI}:latest ."
                }
            }
        }

        stage('Push to AWS ECR') {
            steps {
                script {
                    echo "Authenticating with AWS ECR..."
                    sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
                    
                    echo "Pushing Images to ECR..."
                    sh "docker push ${ECR_URI}:${IMAGE_TAG}"
                    sh "docker push ${ECR_URI}:latest"
                }
            }
        }

        stage('Deploy to ECS Fargate') {
            steps {
                script {
                    echo "🚀 Triggering ECS Rolling Update..."
                    // Forcing a new deployment tells Fargate to pull the fresh 'latest' image we just pushed
                    sh "aws ecs update-service --cluster ${ECS_CLUSTER} --service ${ECS_SERVICE} --force-new-deployment"
                }
            }
        }
    }
}
