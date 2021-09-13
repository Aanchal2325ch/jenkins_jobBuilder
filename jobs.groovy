pipelineJob('job-dsl-plugin') {
  definition {
    cpsScm {
      scm {
        git {
          remote {
            url('https://github.com/Aanchal2325ch/jenkins_jobBuilder.git')
          }
          branch('*/main')
        }
      }
      lightweight()
    }
  }
}
