import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  base: "/",
  plugins: [react()],
  preview: {
    port: 5500,
    strictPort: true,
  },
  server: {
    port: 5500,
    strictPort: true,
    host: true,
    origin: "http://localhost:5500",
  },
});
