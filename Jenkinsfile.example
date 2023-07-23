pipeline {
    agent any
    
    stages {
        stage("Mise à jour Seracia") {
            steps {
                script {
                    withEnv(["PYTHONIOENCODING=UTF-8", "ANSIBLE_SUDO_PASS=jenkins"]) {
                        ansiblePlaybook(
                            colorized: true,
                            credentialsId: 'Github',
                            disableHostKeyChecking: true,
                            installation: 'Ansible',
                            inventory: 'inventory/inventory.ini',
                            playbook: 'seracia.yml',
                            extraVars: [
                                ANSIBLE_HOST_KEY_CHECKING: "False"
                            ],
                            forks: 1
                        )
                    }
                }
            }
        }
    }
}