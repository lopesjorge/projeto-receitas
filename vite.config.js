import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: resolve(__dirname, '../projeto-receitas/base_static/global/js/main.js'),
    },
    outDir: resolve(__dirname, '../projeto-receitas/base_static/global/dist'),
    emptyOutDir: true
  },
   server: {
    host: 'localhost', 
    port: 3000,
    strictPort: true,
  }
})
