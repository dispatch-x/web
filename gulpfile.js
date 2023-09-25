var gulp = require('gulp');
var postcss = require('gulp-postcss');
var sass = require('gulp-sass')(require('sass'));
var cssnano = require('cssnano');
var preset = require('postcss-preset-env');
var magician = require('postcss-font-magician');
var svgo = require('postcss-svgo');
var gulp = require('gulp');
var browserify = require('browserify');
var log = require('gulplog');
var tap = require('gulp-tap');
var buffer = require('gulp-buffer');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
const rcs = require('gulp-rcs');
const replace = require('gulp-replace');
var plumber = require('gulp-plumber');

gulp.task('css', function () {
    var processors = [
		cssnano,
        preset,
        magician,
        svgo
	  ];
	return gulp.src('./assets/styles/scss/*.scss')
		.pipe(sass().on('error', sass.logError))
    .pipe(rcs())
		.pipe(postcss(processors))
		.pipe(gulp.dest('./dist/css'));
});

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

    .pipe(rcs())

    .pipe(uglify())

    // write sourcemaps
    .pipe(sourcemaps.write('./'))

    .pipe(gulp.dest('./dist/js'));

});

gulp.task('remaining', gulp.series('css', 'js', function() {
  return gulp.src(['!./assets/styles/scss/*.scss', '!./assets/js/*.js', './*.html', './tests/*.html'], {base: './'})
    .pipe(rcs())
    .pipe(gulp.dest('./dist/'));
}));

gulp.task('fixpaths', gulp.series('remaining', function () {
  return gulp.src('dist/**/*.html')
    .pipe(plumber())
    .pipe(replace('/assets/styles/css', '/css'))
    .pipe(replace('/assets/js', '/js'))
    .pipe(replace('/assets/img', '/img'))
    .pipe(gulp.dest('./dist'));
}));

gulp.task('default', gulp.series('fixpaths'));
