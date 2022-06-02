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
      // {
      //   use: ['buffer-loader'],
      // },
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
};
