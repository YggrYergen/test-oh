import './globals.css';
import type { ReactNode } from 'react';
import { CartProvider } from '../components/cart-context';

export const metadata = {
  title: 'Verdulería Sostenible',
  description: 'Frescura local y delivery sostenible',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="es-CL">
      <head />
      <body>
        <CartProvider>{children}</CartProvider>
      </body>
    </html>
  );
}
