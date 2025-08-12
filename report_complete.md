# Reporte de Directorio `/home/yggryergen/TYR/test3`

**Generado el:** 2025-08-12 15:01:10

## Estructura de Archivos Incluidos

- .git/
- .next/
  - app-build-manifest.json
  - build-manifest.json
  - package.json
  - prerender-manifest.json
  - react-loadable-manifest.json
  - routes-manifest.json
- README.md
- app/
  - (store)/
    - layout.tsx
    - page.tsx
  - globals.css
  - layout.tsx
- package.json
- postcss.config.js
- tailwind.config.js
- tsconfig.json

---

## .git

**Ruta:** `/home/yggryergen/TYR/test3/.git/`

## .next

**Ruta:** `/home/yggryergen/TYR/test3/.next/`

  ### app-build-manifest.json

  **Tamaño:** 469 bytes, **Última Modificación:** 2025-08-12 14:56:17

  ```json
{
  "pages": {
    "/layout": [
      "static/chunks/webpack.js",
      "static/chunks/main-app.js",
      "static/css/app/layout.css",
      "static/chunks/app/layout.js"
    ],
    "/(store)/layout": [
      "static/chunks/webpack.js",
      "static/chunks/main-app.js",
      "static/chunks/app/(store)/layout.js"
    ],
    "/(store)/page": [
      "static/chunks/webpack.js",
      "static/chunks/main-app.js",
      "static/chunks/app/(store)/page.js"
    ]
  }
}
  ```

  ### build-manifest.json

  **Tamaño:** 388 bytes, **Última Modificación:** 2025-08-12 14:56:17

  ```json
{
  "polyfillFiles": [
    "static/chunks/polyfills.js"
  ],
  "devFiles": [],
  "ampDevFiles": [],
  "lowPriorityFiles": [
    "static/development/_buildManifest.js",
    "static/development/_ssgManifest.js"
  ],
  "rootMainFiles": [
    "static/chunks/webpack.js",
    "static/chunks/main-app.js"
  ],
  "rootMainFilesTree": {},
  "pages": {
    "/_app": []
  },
  "ampFirstPages": []
}
  ```

  ### package.json

  **Tamaño:** 20 bytes, **Última Modificación:** 2025-08-12 14:56:03

  ```json
{"type": "commonjs"}
  ```

  ### prerender-manifest.json

  **Tamaño:** 354 bytes, **Última Modificación:** 2025-08-12 14:56:03

  ```json
{
  "version": 4,
  "routes": {},
  "dynamicRoutes": {},
  "notFoundRoutes": [],
  "preview": {
    "previewModeId": "5e6b67bf44e0cfe08354b96f75493c3d",
    "previewModeSigningKey": "717202d528cd0fabc63f8aaf76e8d54ae609bcb998e65ee00565147c7bc4577f",
    "previewModeEncryptionKey": "541e75e9cd47390877c9c7682ee84d86eb053616396581f5707f52f29a87f109"
  }
}
  ```

  ### react-loadable-manifest.json

  **Tamaño:** 2 bytes, **Última Modificación:** 2025-08-12 14:56:17

  ```json
{}
  ```

  ### routes-manifest.json

  **Tamaño:** 272 bytes, **Última Modificación:** 2025-08-12 14:56:03

  ```json
{"version":3,"caseSensitive":false,"basePath":"","rewrites":{"beforeFiles":[],"afterFiles":[],"fallback":[]},"redirects":[{"source":"/:path+/","destination":"/:path+","permanent":true,"internal":true,"regex":"^(?:\\/((?:[^\\/]+?)(?:\\/(?:[^\\/]+?))*))\\/$"}],"headers":[]}
  ```

### README.md

**Tamaño:** 10 bytes, **Última Modificación:** 2025-08-12 14:19:23

```md
# test-oh

```

## app

**Ruta:** `/home/yggryergen/TYR/test3/app/`

  ## (store)

  **Ruta:** `/home/yggryergen/TYR/test3/app/(store)/`

    ### layout.tsx

    **Tamaño:** 143 bytes, **Última Modificación:** 2025-08-12 14:19:23

    ```tsx
import { PropsWithChildren } from 'react';

export default function StoreLayout({ children }: PropsWithChildren) {
  return <>{children}</>;
}

    ```

    ### page.tsx

    **Tamaño:** 428 bytes, **Última Modificación:** 2025-08-12 14:19:23

    ```tsx
export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-brand-50 p-4">
      <h1 className="text-3xl font-bold text-center text-brand-800 mb-4">
        Frescura local, delivery sostenible
      </h1>
      <p className="text-center text-brand-700">
        Bienvenido a nuestra verdulería. Pronto encontrarás nuestros productos.
      </p>
    </main>
  );
}
    ```

  ### globals.css

  **Tamaño:** 309 bytes, **Última Modificación:** 2025-08-12 14:19:23

  ```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --brand-50: #e9f7ef;
  --brand-100: #d4efdf;
  --brand-200: #a9dfbf;
  --brand-300: #7dce9f;
  --brand-400: #4cbf80;
  --brand-500: #21a368;
  --brand-600: #1a8454;
  --brand-700: #156641;
  --brand-800: #10452f;
  --brand-900: #0b291f;
}

  ```

  ### layout.tsx

  **Tamaño:** 426 bytes, **Última Modificación:** 2025-08-12 14:19:23

  ```tsx
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

  ```

### package.json

**Tamaño:** 595 bytes, **Última Modificación:** 2025-08-12 14:56:02

```json
{
  "name": "verduleria-next15",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build --turbopack",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "framer-motion": "^10.12.17",
    "lucide-react": "^0.259.0",
    "next": "^15.3.0",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "zod": "^3.22.4"
  },
  "devDependencies": {
    "@types/node": "24.2.1",
    "@types/react": "19.1.10",
    "autoprefixer": "^10.4.14",
    "postcss": "^8.4.21",
    "tailwindcss": "^3.4.8",
    "typescript": "^5.2.2"
  }
}

```

### postcss.config.js

**Tamaño:** 83 bytes, **Última Modificación:** 2025-08-12 14:19:23

```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};

```

### tailwind.config.js

**Tamaño:** 316 bytes, **Última Modificación:** 2025-08-12 14:19:23

```js
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

```

### tsconfig.json

**Tamaño:** 651 bytes, **Última Modificación:** 2025-08-12 14:56:02

```json
{
  "compilerOptions": {
    "target": "esnext",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": false,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "incremental": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "plugins": [
      {
        "name": "next"
      }
    ]
  },
  "include": [
    "**/*.ts",
    "**/*.tsx",
    "next-env.d.ts",
    ".next/types/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}

```

