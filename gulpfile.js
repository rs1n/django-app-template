'use strict';

var autoprefixer = require('autoprefixer');
var del = require('del');
var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var concat = require('gulp-concat');
var imagemin = require('gulp-imagemin');
var postCSS = require('gulp-postcss');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');

// Customize your assets path here
var path = {
  src: {
    images: 'assets/images/**/*',
    scripts: {
      all: 'assets/scripts/**/*.js',
      copy: [
      ],
      join: [
      ]
    },
    styles: {
      all:  'assets/styles/**/*.scss',
      main: 'assets/styles/application.scss'
    }
  },
  dest: {
    images:  'static/{{ app_name }}/images',
    scripts: 'static/{{ app_name }}/scripts',
    styles:  'static/{{ app_name }}/styles'
  }
};

// Clean dest scripts folder
gulp.task('clean:scripts', function() {
  return del([path.dest.scripts]);
});

// Clean dest styles folder
gulp.task('clean:styles', function() {
  return del([path.dest.styles]);
});

// Clean dest images folder
gulp.task('clean:images', function() {
  return del([path.dest.images]);
});

// Clean dest folder
gulp.task('clean', ['clean:scripts', 'clean:styles', 'clean:images']);

// Copy scripts
gulp.task('scripts:copy', ['clean'], function() {
  return gulp.src(path.src.scripts.copy)
    .pipe(sourcemaps.init())
      .pipe(uglify())
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(path.dest.scripts));
});

// Concat scripts
gulp.task('scripts:join', ['clean'], function() {
  return gulp.src(path.src.scripts.join)
    .pipe(sourcemaps.init())
      .pipe(uglify())
      .pipe(concat('application.js'))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(path.dest.scripts));
});

// Process scripts
gulp.task('scripts', ['scripts:copy', 'scripts:join']);

// Process SASS
gulp.task('styles', ['clean'], function () {
  return gulp.src(path.src.styles.main)
    .pipe(sourcemaps.init())
      .pipe(sass().on('error', sass.logError))
      .pipe(postCSS([autoprefixer()]))
      .pipe(cleanCSS())
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(path.dest.styles));
});

// Copy all static images
gulp.task('images', ['clean'], function() {
  return gulp.src(path.src.images)
    .pipe(imagemin())
    .pipe(gulp.dest(path.dest.images));
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch([
    path.src.scripts.all, path.src.styles.all, path.src.images
  ], ['scripts', 'styles', 'images']);
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'scripts', 'styles', 'images']);
