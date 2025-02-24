module.exports = {
  content: [
    './portfolio/templates/**/*.html',
    './portfolio/static/**/*.py',
    './portfolio/**/*.py',
    './portfolio/views/**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        'amazon-dark': '#232F3E',
        'amazon-orange': '#FF9900',
        'amazon-light': '#000000',  // Updated to match About's black
      },
    },
  },
  plugins: [],
}