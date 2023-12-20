#!groovy
env.RELEASE_COMMIT = "1"
env.VERSION_NAME = ""
env.SERVICE_NAME = "flask-swagger-generator"
env.REPOSITORY_NAME = "flask-swagger-generator"

pipeline {
    agent none
    stages {
        stage('CheckBranch') {
            agent any
            steps {
                script {
                    result = sh(script: "git log -1 | grep 'Triggered Build'", returnStatus: true)
                    echo 'result ' + result
                    env.RELEASE_COMMIT = result == 0 ? '0' : '1'
                }
            }
        }
        stage('Notificar início de build') {
            agent any
            when {
                expression { env.RELEASE_COMMIT != '0' }
            }
            steps {
                script {
                    withCredentials([string(credentialsId: 'csctracker_token', variable: 'token_csctracker')]) {
                        httpRequest acceptType: 'APPLICATION_JSON',
                                contentType: 'APPLICATION_JSON',
                                httpMode: 'POST', quiet: true,
                                requestBody: '''{
                                                       "app" : "Jenkins",
                                                       "text" : "New build on service ''' + env.SERVICE_NAME + ''' branch ''' + env.BRANCH_NAME + ''' started"
                                                    }''',
                                customHeaders: [[name: 'authorization', value: 'Bearer ' + env.token_csctracker]],
                                url: 'https://gtw.csctracker.com/notify-sync/message'
                    }
                }
            }
        }
        stage('Gerar versão') {
            agent any
            when {
                expression { env.RELEASE_COMMIT != '0' }
            }
            steps {
                script {
                    echo 'RELEASE_COMMIT ' + env.RELEASE_COMMIT
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Master'
                        VERSION = VersionNumber(versionNumberString: '${BUILD_DATE_FORMATTED, "yy"}.${BUILD_WEEK,XX}.${BUILDS_THIS_WEEK,XXX}')
                    } else {
                        echo 'Dev'
                        VERSION = VersionNumber(versionNumberString: '${BUILD_DATE_FORMATTED, "yyyyMMdd"}.${BUILDS_TODAY,XX}.${BUILD_NUMBER,XXXXX}')
                        VERSION = VERSION + '-SNAPSHOT'
                    }
                    script {
                        withCredentials([usernamePassword(credentialsId: 'gitHub', passwordVariable: 'password', usernameVariable: 'user')]) {
                            script {
                                sh 'git pull https://krlsedu:${password}@github.com/krlsedu/' + env.REPOSITORY_NAME + '.git HEAD:' + env.BRANCH_NAME
                                sh 'echo ' + VERSION + ' > version.txt'
                            }
                        }
                    }
                    env.VERSION_NAME = VERSION
                }
            }
        }
        stage('Build') {
            agent any
            when {
                expression { env.RELEASE_COMMIT != '0' }
            }
            steps {
                withPythonEnv('/usr/bin/python3.9') {
                    sh 'python3.9 -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                    sh 'pip install wheel'
                    sh 'python3.9 ./setup.py sdist bdist_wheel'
                }
            }
        }
        stage('Confirmar versão') {
            agent any
            when {
                expression { env.RELEASE_COMMIT != '0' }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'gitHub', passwordVariable: 'password', usernameVariable: 'user')]) {
                        script {
                            echo "Commiting version"
                            if (env.BRANCH_NAME == 'main') {
                                sh "git diff"
                                sh "git add ."
                                sh "git config --global user.email 'krlsedu@gmail.com'"
                                sh "git config --global user.name 'Carlos Eduardo Duarte Schwalm'"
                                sh "git commit -m 'Triggered Build: " + env.VERSION_NAME + "'"
                                sh 'git push https://krlsedu:${password}@github.com/krlsedu/' + env.REPOSITORY_NAME + '.git HEAD:' + env.BRANCH_NAME
                            }
                        }
                    }
                }
            }
        }

        stage('Notificar fim de build') {
            agent any
            when {
                expression { env.RELEASE_COMMIT != '0' }
            }
            steps {
                script {
                    withCredentials([string(credentialsId: 'csctracker_token', variable: 'token_csctracker')]) {
                        httpRequest acceptType: 'APPLICATION_JSON',
                                contentType: 'APPLICATION_JSON',
                                httpMode: 'POST', quiet: true,
                                requestBody: '''{
                                                       "app" : "Jenkins",
                                                       "text" : "Build on service ''' + env.SERVICE_NAME + ''' branch ''' + env.BRANCH_NAME + ''' finished"
                                                    }''',
                                customHeaders: [[name: 'authorization', value: 'Bearer ' + env.token_csctracker]],
                                url: 'https://gtw.csctracker.com/notify-sync/message'
                    }
                }
            }
        }
    }
}
