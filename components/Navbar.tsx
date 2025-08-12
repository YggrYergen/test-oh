'use client';

import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="bg-brand-50 p-4 flex justify-around">
      <Link href="/">Home</Link>
      <Link href="/productos">Productos</Link>
      <Link href="/carro">Carro</Link>
      <Link href="/checkout">Checkout</Link>
      <Link href="/about">About</Link>
    </nav>
  );
}
