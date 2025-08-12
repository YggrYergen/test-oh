import './globals.css';
import { PropsWithChildren } from 'react';

export const metadata = {
  title: 'Verdulería Sostenible',
  description: 'Frescura local, delivery sostenible',
};

export default function RootLayout({ children }: PropsWithChildren) {
  return (
    <html lang="es">
      <head />
      <body className="font-sans antialiased bg-brand-50 text-black">
        {children}
      </body>
    </html>
  );
}
