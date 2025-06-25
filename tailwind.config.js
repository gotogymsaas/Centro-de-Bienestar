/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./src/**/*.{js,jsx}'],
  content: [
    "./templates/**/*.html",
    "./**/*.py",
    "./static/**/*.js",
    "./static/**/*.css",
  ],
  theme: {
    extend: {
      colors: {
        dorado: '#D4B46A',
        grafito: '#101012',
        esmeralda: '#1A9B76',
        plata: '#E0E3E6',
        zafiro: '#17375C',
        turquesa: '#0FBFB0',
        blancoPremium: '#F8F9FA',
        solarYellow: '#F5DF4D',
        skyBlue: '#2D68C4',
        neonPink: '#FF2CD0',
        darkBg: '#111111',
      },
      fontFamily: {
        sans: ['Outfit', 'sans-serif'],
        serif: ['"Playfair Display"', 'serif'],
        header: ['Montserrat', 'sans-serif'],
        body: ['Open Sans', 'sans-serif'],
      },
      boxShadow: {
        luxury: '0 8px 30px rgba(212, 180, 106, 0.2)',
      },
      animation: {
        fadeIn: 'fadeIn 1s ease-out forwards',
        slideUp: 'slideUp 1.2s ease-out forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        slideUp: {
          '0%': { opacity: 0, transform: 'translateY(20px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
      },
      // Puedes agregar aquí tus breakpoints personalizados
      screens: {
        'xs': '480px',
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),    // Eliminamos o comentamos plugins que no vamos a usar:
    // require('@tailwindcss/forms'),
    // require('@tailwindcss/typography'),
    // require('tailwindcss-animate'),
  ],
}

