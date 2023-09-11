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