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

var browserify = require('browserify');
var source = require('vinyl-source-stream');

gulp.task('js', function() {
	var browserified = transform(function(filename) {
		return browserify(filename).bundle();
	});
    //Pass desired output filename to vinyl-source-stream
    return gulp.src('./assets/scripts/js/*.js')
		.pipe(browserified)
		.pipe(gulp.dest('./assets/scripts/js/'));
		// TODO: test
});