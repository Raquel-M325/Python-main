CREATE TABLE ENDERECO
(
  rua INT NOT NULL,
  pais INT NOT NULL,
  bairro INT,
  cep INT NOT NULL,
  numero INT NOT NULL,
  cidade INT NOT NULL,
  estado INT NOT NULL,
  tipo_casa INT,
  id_endereco INT NOT NULL,
  PRIMARY KEY (id_endereco)
);

CREATE TABLE CLIENTE
(
  tipo_pessoa INT NOT NULL,
  cpf INT NOT NULL,
  telefone INT NOT NULL,
  email INT NOT NULL,
  id_endereco INT NOT NULL,
  PRIMARY KEY (cpf),
  FOREIGN KEY (id_endereco) REFERENCES ENDERECO(id_endereco)
);

CREATE TABLE PRODUTO
(
  nome_produto INT NOT NULL,
  preco_produto INT NOT NULL,
  observacoes INT,
  quantidade INT NOT NULL,
  subtotal_produto INT NOT NULL,
  PRIMARY KEY (nome_produto)
);

CREATE TABLE FRETE
(
  preco_frete INT NOT NULL,
  dh_entrega INT NOT NULL,
  empresa_envio INT NOT NULL,
  id_frete INT NOT NULL,
  PRIMARY KEY (id_frete)
);

CREATE TABLE PAGAMENTO
(
  tipos_pagamento INT NOT NULL,
  numero_cartao INT NOT NULL,
  nome_titular INT NOT NULL,
  vencimento INT NOT NULL,
  codigo_seguranca INT NOT NULL,
  id_pagamento INT NOT NULL,
  PRIMARY KEY (id_pagamento)
);

CREATE TABLE CARRINHO
(
  cupom INT NOT NULL,
  subtotal_carrinho INT NOT NULL,
  total_carrinho INT NOT NULL,
  id_carrinho INT NOT NULL,
  cpf INT NOT NULL,
  id_frete INT NOT NULL,
  id_pagamento INT NOT NULL,
  PRIMARY KEY (id_carrinho),
  FOREIGN KEY (cpf) REFERENCES CLIENTE(cpf),
  FOREIGN KEY (id_frete) REFERENCES FRETE(id_frete),
  FOREIGN KEY (id_pagamento) REFERENCES PAGAMENTO(id_pagamento)
);

CREATE TABLE TEM
(
  id_carrinho INT NOT NULL,
  nome_produto INT NOT NULL,
  PRIMARY KEY (id_carrinho, nome_produto),
  FOREIGN KEY (id_carrinho) REFERENCES CARRINHO(id_carrinho),
  FOREIGN KEY (nome_produto) REFERENCES PRODUTO(nome_produto)
);