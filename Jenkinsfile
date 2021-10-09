pipeline {
  agent any
  stages {
    stage('Inicio_env') {
      steps {
        echo 'Iniciando construccion'
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

    stage('Run container') {
      steps {
        sh 'cat versionImage | xargs ./scripts/run.sh'
      }
    }

    stage('Test') {
      steps {
        echo 'Prueba'
        sleep 5
        sh './scripts/test.sh'
      }
    }

    stage('Stop container') {
      steps {
        sh './scripts/stop.sh'
      }
    }

    stage('Publish Hub') {
      steps {
        sh 'cat versionImage | xarg ./scripts/upload.sh'
      }
    }

  }
}