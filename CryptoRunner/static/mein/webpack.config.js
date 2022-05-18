const path = require('path');
const  fileContent  = require ('buffer-loader');

module.exports = {
  mode: 'development',
  entry: './resurs/js.js',
  output: {
    path: path.resolve(__dirname, 'resursJS'),
    filename: 'bundle.js',
  },

  // module: {
  //   rules: [
  //     {
  //       use: ['buffer-loader'],
  //     },
  //   ],
  // },
};
