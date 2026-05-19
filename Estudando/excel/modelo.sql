CREATE TABLE USUARIO
(
  nome INT NOT NULL,
  email_usuario INT NOT NULL,
  senha INT NOT NULL,
  login INT NOT NULL,
  matricula INT,
  PRIMARY KEY (email_usuario)
);

CREATE TABLE ORIENTADOR
(
  email_usuario INT NOT NULL,
  FOREIGN KEY (email_usuario) REFERENCES USUARIO(email_usuario)
);

CREATE TABLE FASE
(
  pds INT NOT NULL
);

CREATE TABLE STATUS
(
  momento INT NOT NULL
);

CREATE TABLE PROJETO
(
  avaliacao INT NOT NULL,
  descricao INT NOT NULL,
  titulo_projeto INT NOT NULL,
  data_criacao INT NOT NULL,
  data_finalizacao INT NOT NULL,
  data_publicacao INT NOT NULL,
  resumo INT NOT NULL,
  imagem INT NOT NULL,
  repositorio INT NOT NULL,
  ,
  ,
  ,
  PRIMARY KEY (titulo_projeto),
  FOREIGN KEY () REFERENCES ORIENTADOR(),
  FOREIGN KEY () REFERENCES FASE(),
  FOREIGN KEY () REFERENCES STATUS()
);

CREATE TABLE ORIENTANDO
(
  matrícula_orientando INT NOT NULL,
  email INT NOT NULL,
  PRIMARY KEY (matrícula_orientando),
  FOREIGN KEY (email) REFERENCES USUARIO(email_usuario)
);

CREATE TABLE PLATAFORMA
(
  tipo INT NOT NULL
);

CREATE TABLE TECNOLOGIA
(
  nome INT NOT NULL,
  icone INT NOT NULL,
  PRIMARY KEY (nome)
);

CREATE TABLE AVALIAR
(
  nota INT NOT NULL,
  comentario INT NOT NULL,
  titulo_projeto INT NOT NULL,
  email_usuario INT NOT NULL,
  PRIMARY KEY (titulo_projeto, email_usuario),
  FOREIGN KEY (titulo_projeto) REFERENCES PROJETO(titulo_projeto),
  FOREIGN KEY (email_usuario) REFERENCES USUARIO(email_usuario)
);

CREATE TABLE PARTICIPA
(
  situacao INT NOT NULL,
  matrícula_orientando INT NOT NULL,
  titulo_projeto INT NOT NULL,
  PRIMARY KEY (matrícula_orientando, titulo_projeto),
  FOREIGN KEY (matrícula_orientando) REFERENCES ORIENTANDO(matrícula_orientando),
  FOREIGN KEY (titulo_projeto) REFERENCES PROJETO(titulo_projeto)
);

CREATE TABLE FAVORITAR
(
  titulo_projeto INT NOT NULL,
  email_usuario INT NOT NULL,
  PRIMARY KEY (titulo_projeto, email_usuario),
  FOREIGN KEY (titulo_projeto) REFERENCES PROJETO(titulo_projeto),
  FOREIGN KEY (email_usuario) REFERENCES USUARIO(email_usuario)
);

CREATE TABLE CATEGORIA
(
  id_principal INT NOT NULL,
  id_subcategoria INT NOT NULL,
  PRIMARY KEY (id_principal, id_subcategoria),
  FOREIGN KEY (id_principal) REFERENCES PROJETO(titulo_projeto),
  FOREIGN KEY (id_subcategoria) REFERENCES PROJETO(titulo_projeto)
);

CREATE TABLE ASSOCIADO
(
  titulo_projeto INT NOT NULL,
  ,
  PRIMARY KEY (titulo_projeto, ),
  FOREIGN KEY (titulo_projeto) REFERENCES PROJETO(titulo_projeto),
  FOREIGN KEY () REFERENCES PLATAFORMA()
);

CREATE TABLE POSSUI
(
  nome_tecnologia INT NOT NULL,
  titulo_projeto INT NOT NULL,
  PRIMARY KEY (nome_tecnologia, titulo_projeto),
  FOREIGN KEY (nome_tecnologia) REFERENCES TECNOLOGIA(nome),
  FOREIGN KEY (titulo_projeto) REFERENCES PROJETO(titulo_projeto)
);

CREATE TABLE PROJETO_CONTATO
(
  contato INT NOT NULL,
  titulo INT NOT NULL,
  PRIMARY KEY (contato, titulo),
  FOREIGN KEY (titulo) REFERENCES PROJETO(titulo_projeto)
);