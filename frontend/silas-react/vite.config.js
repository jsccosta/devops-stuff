import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(
    
  )],
  server:{
    // watch: {
    //   usePolling: true
    // },
    port: 8080,
    strictPort: true,
    host: true,
    origin: "http://0.0.0.0:8080"
  }
})
