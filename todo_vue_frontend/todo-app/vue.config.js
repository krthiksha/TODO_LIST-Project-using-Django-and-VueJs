const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // configuration for production purpose
  publicPath: './',
  outputDir: 'dist'
})


// vercel.json --- file used to mention the standards of app to make the vercel platform understand better about the vueJs and its routing paths etc...
// npm run build --- run this command to generate the build files (test it locally  to ensure it works efficiently -- as vercel generates this files automatically)

