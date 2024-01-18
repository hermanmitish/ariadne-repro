# This autogenerates graphql server from schema.prisma
npm run prisma
# This runs the server in a separate process
npm run dev &
# Finally, we run the codegen and test python client
npm run codegen && ariadne-codegen && python main.py
