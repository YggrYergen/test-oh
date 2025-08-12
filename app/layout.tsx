import './globals.css';
import type { ReactNode } from 'react';

export const metadata = {
  title: 'Verdulería Sostenible',
  description: 'Frescura local y delivery sostenible',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="es-CL">
      <head />
      <body>{children}</body>
    </html>
  );
}
