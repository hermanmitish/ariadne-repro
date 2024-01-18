import { ApolloServer } from "apollo-server-express";
import { setDefaultResultOrder } from "dns";
import { config } from "dotenv";
import * as express from "express";
import { createServer } from "http";
import "reflect-metadata";
import { buildSchema } from "type-graphql";
import { PrismaClient } from "./generated/client";
import { resolvers } from "./generated/typegraphql";
config();
setDefaultResultOrder("ipv4first");

export const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.MONGO_DB,
    },
  },
});

export async function bootstrap() {
  const app = express();
  const httpServer = createServer(app);
  const PORT = 4000;

  const schema = await buildSchema({
    resolvers: resolvers,
    validate: false,
  });

  const server = new ApolloServer({
    schema,
    context: (ctx) => ({ prisma, ...ctx }),
    cache: "bounded",
  });

  await server.start();

  server.applyMiddleware({
    app,
    path: "/v1/graphql",
    cors: { credentials: true },
  });

  await new Promise<void>((resolve) =>
    httpServer.listen({ port: PORT }, () => {
      resolve();
    })
  );

  console.log(`API-Gateway is running on http://localhost:${PORT}`);
}

bootstrap();
