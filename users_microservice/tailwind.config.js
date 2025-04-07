/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/*.py",  // Opcional, para capturar clases en tus archivos Python si se generan dinámicamente
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

