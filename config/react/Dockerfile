FROM node:18

WORKDIR /app

COPY ./frontend /app/

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]

#COPY ./frontend/package*.json ./
#
#RUN npm install
#
#COPY ./frontend /app/
#
#RUN npm run build
#
#EXPOSE 3000
#
#CMD ["npm", "start"]
