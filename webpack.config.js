var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  entry: path.join(__dirname, "app/assets/src/js/index"),
  output: {
    path: path.join(__dirname, "app/assets/dist"),
    filename: "[name].js"
  },
  plugins: [
    new BundleTracker({
      path:  path.join(__dirname, "app/assets"),
      filename: "webpack-stats.json"
    })
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        loader: ["style-loader", "css-loader"]
      }
    ]
  }
};
