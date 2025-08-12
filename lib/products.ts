import products from '../data/products.json';

export interface Product {
  id: number;
  slug: string;
  nombre: string;
  categoria: string;
  unidad: 'kg' | 'unid';
  precioCLP: number;
  stock: number;
  imagen: string;
  organico: boolean;
  destacado: boolean;
}

export function getAllProducts(): Product[] {
  return products as Product[];
}

export function getFeatured(): Product[] {
  return (products as Product[]).filter(p => p.destacado);
}

export function getBySlug(slug: string): Product | undefined {
  return (products as Product[]).find(p => p.slug === slug);
}
