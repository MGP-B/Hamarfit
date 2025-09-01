-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-09-2025 a las 23:01:31
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 7.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hamarfit`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `beneficios`
--

CREATE TABLE `beneficios` (
  `id_beneficio` int(11) NOT NULL,
  `nombre_beneficio` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `id_plan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `nombre_cliente` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `apellido_cliente` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `tipo_documento` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `documento_cliente` varchar(13) COLLATE utf8_spanish_ci NOT NULL,
  `correo_cliente` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `telefono_cliente` char(12) COLLATE utf8_spanish_ci NOT NULL,
  `direccion_cliente` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `inscripcion` date NOT NULL,
  `contrasena_cliente` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `id_plan` int(11) NOT NULL,
  `id_sucursal` int(11) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `nombre_cliente`, `apellido_cliente`, `tipo_documento`, `documento_cliente`, `correo_cliente`, `telefono_cliente`, `direccion_cliente`, `inscripcion`, `contrasena_cliente`, `id_plan`, `id_sucursal`, `id_estado`) VALUES
(8, 'Winnar', 'Peralta', 'DNI', '40219260863', 'winnarperalta5@gmail.com', '8093604545', 'El dorado 1', '2025-09-01', '123456', 2, 1, 1),
(24, 'Luis', 'Martínez', 'DNI', '123456789', 'luis@example.com', '8091234567', 'Calle 1', '2025-08-12', 'segura123', 1, 1, 1),
(28, 'Juan', 'Paredes', 'DNI', '402-1243265-1', 'jpa@gmail.com', '839-020-3443', 'Hacagua', '2025-08-13', '123456', 2, 4, 1),
(29, 'Juan', 'Felipe', 'DNI', '402-9162860-3', 'jfelipe@gmail.com', '829-000-0000', 'Guachupita', '2025-09-01', '123', 1, 4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'sessions', '0001_initial', '2025-08-05 17:51:48.439032');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('uqtl5jla48tsv58ik3svmucozpyftssx', 'eyJjbGllbnRlX2lkIjoyOX0:1utBdD:DWZ2GkZvmR3QpyYYXvsfLS2D4TWrFIEVm3crneq-Xsg', '2025-09-15 21:00:03.731277');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id_empleado` int(11) NOT NULL,
  `nombre_empleado` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `apellido_empleado` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `tipo-documento` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `documento_empleado` varchar(13) COLLATE utf8_spanish_ci NOT NULL,
  `correo_empleado` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `telefono_empleado` varchar(12) COLLATE utf8_spanish_ci NOT NULL,
  `direccion_empleado` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `contratacion_empleado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `contrasena_empleado` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `id_rol` int(11) NOT NULL,
  `id_sucursal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `nombre_empleado`, `apellido_empleado`, `tipo-documento`, `documento_empleado`, `correo_empleado`, `telefono_empleado`, `direccion_empleado`, `contratacion_empleado`, `contrasena_empleado`, `id_rol`, `id_sucursal`) VALUES
(1, 'Winnar', 'Peralta', 'DNI', '402-1926806-3', 'winnarperalta3@gmail.com', '829-332-0768', 'El Dorado', '2025-08-01 00:00:00', '123', 1, 1),
(3, 'Weslling', 'Garcia', 'DNI', '402-2936816-3', 'weslling@gmail.com', '829-489-0880', 'Lejos', '2025-01-01 00:00:00', '123454321', 2, 1),
(9, 'Masembe', 'Mohammed', 'Pasaporte', '09182308-5', 'masembe@gmail.com', '000-000-0019', 'Africa', '2025-02-21 00:00:00', '00000000', 3, 1),
(10, 'Juan', 'Soto', 'DNI', '40285268984', 'juansoto123@gmail.com', '8294568787', 'Santiago', '2025-09-01 00:00:00', '123', 4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE `estados` (
  `id_estado` int(11) NOT NULL,
  `estado` varchar(10) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`id_estado`, `estado`) VALUES
(1, 'Activo'),
(2, 'Inactivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripciones_renovaciones`
--

CREATE TABLE `inscripciones_renovaciones` (
  `id_finanza` int(11) NOT NULL,
  `emision` date NOT NULL,
  `descripcion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_metodo` int(11) NOT NULL,
  `id_plan` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `inscripciones_renovaciones`
--

INSERT INTO `inscripciones_renovaciones` (`id_finanza`, `emision`, `descripcion`, `id_empleado`, `id_metodo`, `id_plan`, `id_cliente`) VALUES
(2, '2025-08-13', 'Renovación', 1, 1, 1, 24),
(3, '2025-08-13', 'Renovación', 1, 1, 1, 8),
(4, '2025-08-13', 'Inscripción', 1, 1, 2, 28),
(5, '2025-09-01', 'Inscripción', 1, 1, 1, 29),
(6, '2025-09-01', 'Renovación', 1, 1, 1, 29);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodos_pagos`
--

CREATE TABLE `metodos_pagos` (
  `id_metodo` int(11) NOT NULL,
  `metodo` varchar(40) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `metodos_pagos`
--

INSERT INTO `metodos_pagos` (`id_metodo`, `metodo`) VALUES
(1, 'Efectivo'),
(2, 'Tarjeta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nota_clientes`
--

CREATE TABLE `nota_clientes` (
  `id_nota` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `nota` varchar(800) COLLATE utf8_spanish_ci NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `nota_clientes`
--

INSERT INTO `nota_clientes` (`id_nota`, `fecha`, `nota`, `id_cliente`) VALUES
(2, '2025-08-26', 'Tiene problemas en la rodilla derecha', 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id_permiso` int(11) NOT NULL,
  `permiso` varchar(80) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `planes`
--

CREATE TABLE `planes` (
  `id_plan` int(11) NOT NULL,
  `nombre_plan` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `mensualidad` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `planes`
--

INSERT INTO `planes` (`id_plan`, `nombre_plan`, `mensualidad`) VALUES
(1, 'Básico', 1500),
(2, 'Pro', 2000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `rol` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(300) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `rol`, `descripcion`) VALUES
(1, 'Admin', 'Tiene acceso a todo'),
(2, 'Gerente', 'Tiene acceso a todos los apartados pero no puede eliminar usuarios ni acceder a la base de datos'),
(3, 'Entrenador', 'Solo tiene acceso a los clientes pero no puede agregarlos'),
(4, 'Recepcionista', 'Tiene acceso a clientes y transacciones');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles_permisos`
--

CREATE TABLE `roles_permisos` (
  `id_rol` int(11) NOT NULL,
  `id_permiso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sucursales`
--

CREATE TABLE `sucursales` (
  `id_sucursal` int(11) NOT NULL,
  `nombre_sucursal` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `direccion_sucursal` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `telefono_sucursal` varchar(12) COLLATE utf8_spanish_ci NOT NULL,
  `hora_apertura` time NOT NULL,
  `hora_cierre` time NOT NULL,
  `imagen` varchar(200) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `sucursales`
--

INSERT INTO `sucursales` (`id_sucursal`, `nombre_sucursal`, `direccion_sucursal`, `telefono_sucursal`, `hora_apertura`, `hora_cierre`, `imagen`) VALUES
(1, 'HamarFit Central', 'Av. Principal #21, Santiago', '809-222-0908', '05:00:00', '21:00:00', 'productos/25/08/11/Central_Hamarfit.png'),
(4, 'HamarFit Quinigua', 'Quinigua', '829-009-2919', '05:00:00', '21:00:00', 'productos/25/08/11/estufa_de_induccion.png'),
(5, 'Hamarfit Jacagua', 'Jacagua', '829-008-8800', '05:00:00', '21:00:00', 'productos/25/08/14/Central_Hamarfit.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `beneficios`
--
ALTER TABLE `beneficios`
  ADD PRIMARY KEY (`id_beneficio`),
  ADD KEY `beneficio` (`id_plan`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`),
  ADD KEY `plan` (`id_plan`),
  ADD KEY `id_sucursal` (`id_sucursal`),
  ADD KEY `id_estado_2` (`id_estado`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id_empleado`),
  ADD KEY `rol` (`id_rol`),
  ADD KEY `sucursal` (`id_sucursal`);

--
-- Indices de la tabla `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `inscripciones_renovaciones`
--
ALTER TABLE `inscripciones_renovaciones`
  ADD PRIMARY KEY (`id_finanza`),
  ADD KEY `empleado` (`id_empleado`),
  ADD KEY `id_metodo` (`id_metodo`),
  ADD KEY `id_plan` (`id_plan`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Indices de la tabla `metodos_pagos`
--
ALTER TABLE `metodos_pagos`
  ADD PRIMARY KEY (`id_metodo`);

--
-- Indices de la tabla `nota_clientes`
--
ALTER TABLE `nota_clientes`
  ADD PRIMARY KEY (`id_nota`),
  ADD KEY `nota` (`id_cliente`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id_permiso`);

--
-- Indices de la tabla `planes`
--
ALTER TABLE `planes`
  ADD PRIMARY KEY (`id_plan`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `roles_permisos`
--
ALTER TABLE `roles_permisos`
  ADD UNIQUE KEY `id_rol` (`id_rol`),
  ADD UNIQUE KEY `id_permiso` (`id_permiso`);

--
-- Indices de la tabla `sucursales`
--
ALTER TABLE `sucursales`
  ADD PRIMARY KEY (`id_sucursal`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `beneficios`
--
ALTER TABLE `beneficios`
  MODIFY `id_beneficio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `estados`
--
ALTER TABLE `estados`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `inscripciones_renovaciones`
--
ALTER TABLE `inscripciones_renovaciones`
  MODIFY `id_finanza` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `metodos_pagos`
--
ALTER TABLE `metodos_pagos`
  MODIFY `id_metodo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `nota_clientes`
--
ALTER TABLE `nota_clientes`
  MODIFY `id_nota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id_permiso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `planes`
--
ALTER TABLE `planes`
  MODIFY `id_plan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sucursales`
--
ALTER TABLE `sucursales`
  MODIFY `id_sucursal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `beneficios`
--
ALTER TABLE `beneficios`
  ADD CONSTRAINT `beneficio` FOREIGN KEY (`id_plan`) REFERENCES `planes` (`id_plan`);

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`id_sucursal`) REFERENCES `sucursales` (`id_sucursal`),
  ADD CONSTRAINT `clientes_ibfk_2` FOREIGN KEY (`id_estado`) REFERENCES `estados` (`id_estado`),
  ADD CONSTRAINT `plan` FOREIGN KEY (`id_plan`) REFERENCES `planes` (`id_plan`);

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `rol` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`),
  ADD CONSTRAINT `sucursal` FOREIGN KEY (`id_sucursal`) REFERENCES `sucursales` (`id_sucursal`);

--
-- Filtros para la tabla `inscripciones_renovaciones`
--
ALTER TABLE `inscripciones_renovaciones`
  ADD CONSTRAINT `empleado` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id_empleado`),
  ADD CONSTRAINT `id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE CASCADE,
  ADD CONSTRAINT `id_metodo` FOREIGN KEY (`id_metodo`) REFERENCES `metodos_pagos` (`id_metodo`),
  ADD CONSTRAINT `id_plan` FOREIGN KEY (`id_plan`) REFERENCES `planes` (`id_plan`);

--
-- Filtros para la tabla `nota_clientes`
--
ALTER TABLE `nota_clientes`
  ADD CONSTRAINT `nota` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`);

--
-- Filtros para la tabla `roles_permisos`
--
ALTER TABLE `roles_permisos`
  ADD CONSTRAINT `roles_permisos_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`),
  ADD CONSTRAINT `roles_permisos_ibfk_2` FOREIGN KEY (`id_permiso`) REFERENCES `permisos` (`id_permiso`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
