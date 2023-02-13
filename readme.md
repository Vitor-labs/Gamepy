## Requisitos Funcionais

- [*x*] O usuário deverá fazer login
- [*x*] O usuário poderá adicionar e remover produtos do carrinho.
- [*x*] O usuário poderá ordenar os produtos por preço, popularidade (score) e ordem alfabética. A filtragem deve ser realizada pela API.
- [] Os valores exibidos no checkout (frete, subtotal e total) devem ser calculados dinamicamente conforme o usuário seleciona ou remove produtos.
- [] A cada produto adicionado, deve-se somar R$ 10,00 ao frete.
- [] Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.
- [] O usuário pode realizar checkout de seu carrinho de compras. 
- [] O usuário pode consultar os pedidos feitos.

## Requisitos Não Funcionais

- [*x*] Deverá ser documentado no [README.md](./README.md) como executar/compilar/empacotar o projeto e quais os endpoints solicitados nos requisitos acima. Para esse fim podem ser utilizadas ferramentas de containerização e automatização de builds.
- [*x*] Utilizar o banco de dados Postgres.
- [*x*] Para CRUD das entidades no banco de dados, utilizar preferencialmente migrations.
