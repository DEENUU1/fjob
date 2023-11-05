FROM node:alpine

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY frontend/ .

EXPOSE 5173

CMD ["npm", "run", "build"]
