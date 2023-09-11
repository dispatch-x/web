/** @type {import('postcss-load-config').Config} */
const config = {
    plugins: [
        postcssPresetEnv({
			/* pluginOptions */
			features: {
				'nesting-rules': {
					noIsPseudoSelector: false,
				},
			},
		})
    ]
}

module.exports = config