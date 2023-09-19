var gulp = require('gulp');
var postcss = require('gulp-postcss');
var sass = require('gulp-sass')(require('sass'));
var cssnano = require('cssnano');
var preset = require('postcss-preset-env');
var magician = require('postcss-font-magician');
var svgo = require('postcss-svgo');
gulp.task('css', function () {
    var processors = [
		cssnano,
        preset,
        magician,
        svgo
	];
	return gulp.src('./assets/styles/scss/*.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(postcss(processors))
		.pipe(gulp.dest('./assets/styles/css'));
});

var gulp = require('gulp');
var browserify = require('browserify');
var log = require('gulplog');
var tap = require('gulp-tap');
var buffer = require('gulp-buffer');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');

gulp.task('js', function () {

  return gulp.src('./assets/js/*.js', {read: false}) // file because browserify does.

    // transform file objects using gulp-tap plugin
    .pipe(tap(function (file) {

      log.info('bundling ' + file.path);

      // replace file contents with browserify's bundle stream
      file.contents = browserify(file.path, {debug: true}).bundle();

    }))

    // transform streaming contents into buffer contents (because gulp-sourcemaps does not support streaming contents)
    .pipe(buffer())

    // load and init sourcemaps
    .pipe(sourcemaps.init({loadMaps: true}))

    .pipe(uglify())

    // write sourcemaps
    .pipe(sourcemaps.write('./'))

    .pipe(gulp.dest('./assets/js/dist'));

});