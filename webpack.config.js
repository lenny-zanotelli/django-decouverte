const path = require('path');

module.exports = {
	entry: './static/js/index.js',
	output: {
		'path': path.resolve(__dirname, 'MyApp', 'static'),
		'filename': 'bundle.js'
	}
}