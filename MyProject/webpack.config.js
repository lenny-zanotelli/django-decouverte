const path = require('path');

module.exports = {
	entry: './static/js/index.js',
	output: {
		path: path.resolve(__dirname, 'MyApp', 'static'),
		filename: 'bundle.js'
	},
	module: {
		rules:[
			{
				test: /\.css$/,
				use: ['style-loader', 'css-loader'],
			},
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: { loader: 'babel-loader',},
			}
		]
	}
};