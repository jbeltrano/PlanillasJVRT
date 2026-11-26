CREATE TABLE "usuario" (
  "nombre" varchar NOT NULL UNIQUE,
  "contraseña" varchar NOT NULL,
  "tipo_usuario" varchar NOT NULL DEFAULT 'usuario',
  CONSTRAINT "usuario_tipo_usuario_valido"
    CHECK ("tipo_usuario" IN ('administrador', 'usuario'))
);

CREATE TABLE "registro_extracto" (
  "nombre_usuario" varchar,
  "extracto_id" varchar,
  "fecha_registro" datetime DEFAULT 'now'
);

CREATE TABLE "conductor" (
  "id" varchar,
  "nombre" text,
  "vigencia" date
);

CREATE TABLE "persona" (
  "id" varchar,
  "tipo_id" varchar,
  "nombre" text,
  "telefono" text,
  "direccion" text
);

CREATE TABLE "vehiculo" (
  "id" varchar,
  "modelo" text,
  "marca" text,
  "clase" text,
  "interno" integer,
  "top" integer
);

CREATE TABLE "extracto" (
  "id" varchar,
  "vehiculo_id" varchar NOT NULL,
  "empresa_id" varchar NOT NULL,
  "contrato" integer NOT NULL,
  "contratante_id" varchar NOT NULL,
  "objeto_contrato" text NOT NULL,
  "recorrido" text NOT NULL,
  "convenio_id" varchar NOT NULL,
  "conductor_1_id" varchar NOT NULL,
  "conductor_2_id" varchar,
  "conductor_3_id" varchar,
  "fecha_inicio" date NOT NULL,
  "fecha_fin" date NOT NULL,
  "responsable_id" varchar NOT NULL
);

ALTER TABLE "registro_extracto" ADD FOREIGN KEY ("nombre_usuario") REFERENCES "usuario" ("nombre") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "registro_extracto" ADD FOREIGN KEY ("extracto_id") REFERENCES "extracto" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("vehiculo_id") REFERENCES "vehiculo" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("empresa_id") REFERENCES "persona" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("contratante_id") REFERENCES "persona" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("convenio_id") REFERENCES "persona" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("conductor_1_id") REFERENCES "conductor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("conductor_2_id") REFERENCES "conductor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("conductor_3_id") REFERENCES "conductor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "extracto" ADD FOREIGN KEY ("responsable_id") REFERENCES "persona" ("id") DEFERRABLE INITIALLY IMMEDIATE;
