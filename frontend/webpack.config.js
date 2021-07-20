const {VueLoaderPlugin} = require("vue-loader");
const path = require('path');

module.exports = {
  entry: {
    admin: './src/admin.js',
  },
  output: {
    filename: '[name].js',
    path: path.join(__dirname, '../static/vue-files'),
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
    ],
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  resolve: {
    // alias: {
    //   vue$: "vue/dist/vue.runtime.esm.js",
    // },
    extensions: ["*", ".js", ".vue", ".json"],
  },
};
