import Navbar from '../../components/Navbar';
export default function StorePage() {
  return (
    <>
      <Navbar />
      <main className="min-h-screen flex items-center justify-center p-4">
        <h1 className="text-3xl font-bold">Frescura local, delivery sostenible</h1>
      </main>
      <footer className="bg-brand-100 p-4 text-center">
        <p>Zona de entrega: Papudo y alrededores</p>
      </footer>
    </>
  );
}
