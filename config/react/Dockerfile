FROM node:18 as build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install
RUN npm install -g serve
COPY frontend/ .

CMD ["npm", "run", "build"]



