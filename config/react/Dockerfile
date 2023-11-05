FROM node:21 as build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY frontend/ .

RUN npm run build

EXPOSE 4173

CMD ["npm", "run", "preview"]
