/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'brand-50': 'var(--brand-50)',
        'brand-100': 'var(--brand-100)',
      },
    },
  },
  plugins: [],
};
