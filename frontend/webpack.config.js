const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: 'development', // Set the mode to development
  entry: './src/index.js', // The entry point of your application
  output: {
    path: path.resolve(__dirname, 'dist'), // The output directory for bundled files
    filename: 'bundle.js', // The name of the bundled file
  },
  devtool: 'source-map', // Generate source maps for easier debugging
  module: {
    rules: [
      {
        test: /\.js$/, // Apply babel-loader to transpile JavaScript files
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/, // Process CSS files using style-loader and css-loader
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({ // Generate HTML file with bundled JavaScript injected
      template: './src/index.html',
      filename: 'index.html',
    }),
    new MiniCssExtractPlugin({ // Extract CSS into separate files
      filename: '[name].css',
      chunkFilename: '[id].css',
    }),
  ],
};

