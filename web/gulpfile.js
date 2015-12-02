var gulp = require('gulp');
var less = require('gulp-less');
var plumber = require('gulp-plumber');

gulp.task('less', function () {
  gulp.src('project/static/less/styles.less')
  .pipe(plumber())
  .pipe(less())
  .pipe(gulp.dest('project/static/css'));
});

gulp.task('watch', function() {
  gulp.watch('project/static/less/**/*.less', ['less']);
});

gulp.task('default', ['less', 'watch']);
