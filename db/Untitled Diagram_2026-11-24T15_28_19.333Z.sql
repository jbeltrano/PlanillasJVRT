CREATE TABLE IF NOT EXISTS "CONDUCTOR" (
	"id" VARCHAR(15) NOT NULL UNIQUE,
	"nombre" TEXT NOT NULL,
	"fecha_vencimiento" DATE NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "VEHICULO" (
	"id" VARCHAR(7) NOT NULL UNIQUE,
	"modelo" INTEGER NOT NULL,
	"marca" TEXT NOT NULL,
	"clase" TEXT NOT NULL,
	"numero_interno" INTEGER NOT NULL,
	"top" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "PERSONA" (
	"id" VARCHAR(15) NOT NULL,
	"nombre" TEXT NOT NULL,
	"telefono" TEXT NOT NULL,
	"direccion" TEXT NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "EXTRACTO" (
	"id" VARCHAR(100) NOT NULL UNIQUE,
	"numero_extracto" TEXT NOT NULL,
	"razon_social" VARCHAR(255) NOT NULL DEFAULT 'LINEAS JAVARTURS DEL LLANO S.A.S.',
	"nit_razon_social" VARCHAR(100) NOT NULL DEFAULT '830.085.825-5',
	"contrato" VARCHAR(20) NOT NULL,
	"contratante" VARCHAR(15) NOT NULL,
	"objeto_contrato" TEXT NOT NULL,
	"origen_destino" TEXT NOT NULL,
	"fecha_inicial" DATE NOT NULL,
	"fecha_final" DATE NOT NULL,
	"vehiculo" VARCHAR(7) NOT NULL,
	"conductor1" VARCHAR(255) NOT NULL,
	"conductor2" VARCHAR(255),
	"conductor3" VARCHAR(255),
	"responsable" VARCHAR(255) NOT NULL,
	PRIMARY KEY("id"),

	CONSTRAINT fk_contratante
		FOREIGN KEY (contratante)
		REFERENCES PERSONA (id),
	
	CONSTRAINT fk_responsable
		FOREIGN KEY (responsable)
		REFERENCES PERSONA (id),

	CONSTRAINT fk_vehiculo
		FOREIGN KEY (vehiculo)
		REFERENCES VEHICULO (id),

	CONSTRAINT fk_conductor_1
		FOREIGN KEY (conductor1)
		REFERENCES CONDUCTOR (id),
	CONSTRAINT fk_conductor_2
		FOREIGN KEY (conductor2)
		REFERENCES CONDUCTOR (id),
	CONSTRAINT fk_conductor_3
		FOREIGN KEY (conductor3)
		REFERENCES CONDUCTOR (id)
);