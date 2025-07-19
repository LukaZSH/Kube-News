# Multi-stage build para otimizar o tamanho da imagem final
FROM node:22-alpine 
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node", "server.js"] 