def sha1

pipeline{
    agent any
    stages{
        stage('Init'){
            steps{
                script{
                    sha1 = sh('git rev-parse --short HEAD', returnStdout=true)
                }
            }
        }
        stage('Build'){
            steps{
                sh "docker build -t edu0:$sha1 ."
                sh "docker build -f Dockerfile-test -t edu0-test:$sha1 ."
            }
        }
        stage('Tests'){
            parallel{
                stage('pylint'){
                    steps{
                        sh "docker container run edu0:$sha1 pylint ."
                    }
                }
                stage('flake8'){
                    steps{
                        sh "docker container run edu0:$sha1 flake8"
                    }
                }
                stage('pytest'){
                    steps{
                        sh "docker container run edu0:$sha1 pytest"
                    }
                }
                stage('bandit') {
                    steps{
                        sh "docker container run edu0:$sha1 bandit -r src"
                    }
                }
            }
        }
    }
}