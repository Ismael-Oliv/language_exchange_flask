
FROM node:18-alpine

WORKDIR /user/src/app

COPY . ./

RUN npm i -g @nestjs/cli

RUN npm install --omit=dev

RUN npm run build

CMD ["npm", "run", "start:prod"]