CREATE TABLE ENDERECO
(
  rua VARCHAR(255) NOT NULL,
  pais VARCHAR(255) NOT NULL,
  bairro VARCHAR(255),
  cep VARCHAR(10) NOT NULL,
  numero_casa INT NOT NULL,
  cidade VARCHAR(255) NOT NULL,
  estado VARCHAR(255) NOT NULL,
  tipo_casa VARCHAR(255),
  id_endereco INT NOT NULL,
  PRIMARY KEY (id_endereco)
);

CREATE TABLE CLIENTE
(
  tipo_pessoa VARCHAR(50) NOT NULL,
  cpf_cliente VARCHAR(15) NOT NULL,
  telefone_cliente VARCHAR(20) NOT NULL,
  email_cliente VARCHAR(255) NOT NULL,
  nome_cliente VARCHAR(255) NOT NULL,
  id_endereco INT NOT NULL,
  PRIMARY KEY (cpf_cliente),
  FOREIGN KEY (id_endereco) REFERENCES ENDERECO(id_endereco)
);

CREATE TABLE PRODUTO
(
  nome_produto VARCHAR(255) NOT NULL,
  preco_produto FLOAT NOT NULL,
  observacoes VARCHAR(255),
  quantidade INT NOT NULL,
  subtotal_produto FLOAT NOT NULL,
  PRIMARY KEY (nome_produto)
);

CREATE TABLE FRETE
(
  preco_frete FLOAT NOT NULL,
  dh_entrega DATE NOT NULL,
  empresa_envio VARCHAR(255) NOT NULL,
  id_frete INT NOT NULL,
  PRIMARY KEY (id_frete)
);

CREATE TABLE PAGAMENTO
(
  tipos_pagamento INT NOT NULL,
  numero_cartao VARCHAR(20) NOT NULL,
  nome_titular VARCHAR(255) NOT NULL,
  vencimento DATE NOT NULL,
  codigo_seguranca VARCHAR(5) NOT NULL,
  id_pagamento INT NOT NULL,
  PRIMARY KEY (id_pagamento)
);

CREATE TABLE CARRINHO
(
  cupom VARCHAR(50) NOT NULL,
  subtotal_carrinho FLOAT NOT NULL,
  total_carrinho FLOAT NOT NULL,
  id_carrinho INT NOT NULL,
  cpf_cliente VARCHAR(15) NOT NULL,
  id_frete INT NOT NULL,
  id_pagamento INT NOT NULL,
  nome_produto VARCHAR(255) NOT NULL,
  PRIMARY KEY (id_carrinho),
  FOREIGN KEY (cpf_cliente) REFERENCES CLIENTE(cpf_cliente),
  FOREIGN KEY (id_frete) REFERENCES FRETE(id_frete),
  FOREIGN KEY (id_pagamento) REFERENCES PAGAMENTO(id_pagamento),
  FOREIGN KEY (nome_produto) REFERENCES PRODUTO(nome_produto)
);