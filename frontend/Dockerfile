# Use a node base image
FROM node:22-alpine as build

# Set the working directory in the container
WORKDIR /app

# Install app dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Bundle app source
COPY . /app

# Build the application
RUN npm run build

# Production environment
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
