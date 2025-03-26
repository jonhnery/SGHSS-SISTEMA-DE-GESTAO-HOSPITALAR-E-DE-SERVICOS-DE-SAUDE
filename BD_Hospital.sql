SHOW DATABASES;
CREATE DATABASE sghss;
USE sghss;

CREATE TABLE Usuario (
    id INT NOT NULL AUTO_INCREMENT,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE SistemaSeguranca (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Autentica (
    idUsuario INT NOT NULL,
    idSistemaSeguranca INT NOT NULL,
    CONSTRAINT fk_autentica_usuario FOREIGN KEY (idUsuario) REFERENCES Usuario(id),
    CONSTRAINT fk_autentica_sistema FOREIGN KEY (idSistemaSeguranca) REFERENCES SistemaSeguranca(id)
);

CREATE TABLE Administrador (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Suprimento (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Gerencia (
    idAdministrador INT NOT NULL,
    idSuprimento INT NOT NULL,
    CONSTRAINT fk_gerencia_adm FOREIGN KEY (idAdministrador) REFERENCES Administrador(id),
    CONSTRAINT fk_gerencia_suprimento FOREIGN KEY (idSuprimento) REFERENCES Suprimento(id)
);

CREATE TABLE Paciente (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    dataNascimento DATE NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Leito (
    id INT NOT NULL AUTO_INCREMENT,
    numero INT NOT NULL,
    status VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE OcupadoPor (
    idPaciente INT NOT NULL,
    idLeito INT NOT NULL,
    CONSTRAINT fk_ocupado_paciente FOREIGN KEY (idPaciente) REFERENCES Paciente(id),
    CONSTRAINT fk_ocupado_leito FOREIGN KEY (idLeito) REFERENCES Leito(id)
);

CREATE TABLE Profissional (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    registro VARCHAR(20) NOT NULL,
    especialidade VARCHAR(50),
    telefone VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE Consulta (
    id INT NOT NULL AUTO_INCREMENT,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    pacienteId INT NOT NULL,
    profissionalId INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_consulta_paciente FOREIGN KEY (pacienteId) REFERENCES Paciente(id),
    CONSTRAINT fk_consulta_profissional FOREIGN KEY (profissionalId) REFERENCES Profissional(id)
);

CREATE TABLE Atende (
    idProfissional INT NOT NULL,
    idConsulta INT NOT NULL,
    CONSTRAINT fk_atende_profissional FOREIGN KEY (idProfissional) REFERENCES Profissional(id),
    CONSTRAINT fk_atende_consulta FOREIGN KEY (idConsulta) REFERENCES Consulta(id)
);

CREATE TABLE Prontuario (
    id INT NOT NULL AUTO_INCREMENT,
    descricao TEXT,
    consultaId INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_prontuario_consulta FOREIGN KEY (consultaId) REFERENCES Consulta(id)
);

CREATE TABLE ReceitaDigital (
    id INT NOT NULL AUTO_INCREMENT,
    data DATE NOT NULL,
    conteudo TEXT,
    consultaId INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_receita_consulta FOREIGN KEY (consultaId) REFERENCES Consulta(id)
);

CREATE TABLE Agenda (
    id INT NOT NULL AUTO_INCREMENT,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    profissionalId INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_agenda_profissional FOREIGN KEY (profissionalId) REFERENCES Profissional(id)
);





