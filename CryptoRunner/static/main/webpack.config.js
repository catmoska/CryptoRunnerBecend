const path = require('path');
const  fileContent  = require ('buffer-loader');

module.exports = {
  mode: 'development',
  entry: './script/init.ts',
  output: {
    path: path.resolve(__dirname, 'resursJS'),
    filename: 'bundle.js',
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
};
