const path = require('path');

module.exports = {
  outputDir: path.join(__dirname, '../static/vue-files'),
  pages: {
    admin: {
      entry: 'src/admin.js',
    },
  },
  // Все js и css в одном файле
  configureWebpack: config => {
    config.output.filename = '[name].js'
    config.output.chunkFilename = '[name].js'
    config.optimization.splitChunks = false;
  },
  css: {
    extract: false,
  },
}
