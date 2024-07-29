# Use an official Node.js LTS (Long Term Support) as a parent image
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /app

ENV PATH="app/node_modules/.bin/path:$PATH"

COPY package*.json ./

RUN npm install 

COPY . .

EXPOSE 8080

CMD ["npm", "run", "dev"]