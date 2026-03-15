module.exports = (grunt) ->
  grunt.initConfig
    docroot: 'test'
    test_host: 'http://localhost'

    clean:
      general: [
        'config.js'
        'doc'
        'docroot'
        'docroot_tmp'
      ]
      test: [
        'test/js'
        'test/*.html'
        '!test/scaffold.html'
      ]

    concat:
      dist:
        src: ['js/**/*.js']
        dest: '<%= docroot %>/lib.js'

    copy:
      lib:
        files: [
          expand: true
          cwd: 'lib'
          src: ['**']
          dest: '<%= docroot %>/lib'
        ]

    'closure-compiler':
      frontend:
        closurePath: 'node_modules/grunt-closure-compiler'
        js: 'test/lib.js'
        jsOutputFile: 'test/lib.min.js'

  # Load grunt tasks that come from other modules.
  #grunt.loadNpmTasks('grunt-contrib-clean')
  #grunt.loadNpmTasks('grunt-contrib-copy')
  #
  grunt.loadNpmTasks('grunt-contrib-concat')
  grunt.loadNpmTasks('grunt-closure-compiler');

  grunt.registerTask('default', ['concat','closure-compiler']);
