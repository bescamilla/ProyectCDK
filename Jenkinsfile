pipeline {
  agent any
  stages {
    stage('Inicio_env') {
      steps {
        echo 'Iniciando construcción'
        sh 'env'
      }
    }

    stage('Docker env') {
      parallel {
        stage('Docker env') {
          steps {
            sh 'docker -v'
          }
        }

        stage('Docker images') {
          steps {
            sh 'docker images'
          }
        }

      }
    }

    stage('build') {
      steps {
        sh 'cat versionImage | xargs ./scripts/build.sh'
      }
    }

  }
}