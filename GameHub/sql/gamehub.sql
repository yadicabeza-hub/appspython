-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS `gamehub_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `gamehub_db`;

-- --------------------------------------------------------
-- Tabla `usuarios`
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre_usuario` VARCHAR(50) NOT NULL UNIQUE,
  `correo` VARCHAR(120) NOT NULL UNIQUE,
  `contrasena_hash` VARCHAR(255) NOT NULL,
  `fecha_registro` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `estado` BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Tabla `perfiles`
-- Relación 1:1 con `usuarios`
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `perfiles` (
  `id_perfil` INT AUTO_INCREMENT PRIMARY KEY,
  `id_usuario` INT NOT NULL UNIQUE,
  `nombre_completo` VARCHAR(120) DEFAULT NULL,
  `fotografia` VARCHAR(255) DEFAULT NULL,
  `biografia` TEXT DEFAULT NULL,
  `pais` VARCHAR(80) DEFAULT NULL,
  `sitio_web` VARCHAR(255) DEFAULT NULL,
  `tipo_usuario` ENUM('jugador', 'desarrollador', 'ambos') DEFAULT 'jugador',
  CONSTRAINT `fk_perfiles_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Tabla `videojuegos`
-- Relación 1:N con `usuarios`
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `videojuegos` (
  `id_videojuego` INT AUTO_INCREMENT PRIMARY KEY,
  `id_usuario` INT NOT NULL,
  `titulo` VARCHAR(150) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `genero` VARCHAR(80) NOT NULL,
  `plataforma` VARCHAR(80) NOT NULL,
  `version` VARCHAR(30) DEFAULT NULL,
  `estado` ENUM('desarrollo', 'demo', 'beta', 'terminado') DEFAULT 'terminado',
  `portada` VARCHAR(255) DEFAULT NULL,
  `archivo_juego` VARCHAR(255) DEFAULT NULL,
  `enlace_descarga` VARCHAR(500) DEFAULT NULL,
  `fecha_publicacion` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `activo` BOOLEAN DEFAULT TRUE,
  CONSTRAINT `fk_videojuegos_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Tabla `resenas`
-- Relaciones 1:N con `usuarios` y 1:N con `videojuegos`
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `resenas` (
  `id_resena` INT AUTO_INCREMENT PRIMARY KEY,
  `id_usuario` INT NOT NULL,
  `id_videojuego` INT NOT NULL,
  `calificacion` INT NOT NULL CHECK (`calificacion` >= 1 AND `calificacion` <= 5),
  `comentario` TEXT NOT NULL,
  `fecha_resena` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_resenas_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_resenas_videojuegos` FOREIGN KEY (`id_videojuego`) REFERENCES `videojuegos` (`id_videojuego`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `uq_usuario_videojuego` UNIQUE (`id_usuario`, `id_videojuego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Registros de prueba iniciales (Opcional)
-- Contraseña hash para 'password123' (generado con bcrypt por defecto)
-- --------------------------------------------------------
INSERT INTO `usuarios` (`nombre_usuario`, `correo`, `contrasena_hash`) VALUES
('admin_demo', 'admin@gamehub.local', '$2b$12$KkQ8r2H18G.T1yDk5V8iT.O1b88p4lQ5/8Y/M3/M.w25rXvP.9v1S'),
('player_one', 'player1@gamehub.local', '$2b$12$KkQ8r2H18G.T1yDk5V8iT.O1b88p4lQ5/8Y/M3/M.w25rXvP.9v1S');

INSERT INTO `perfiles` (`id_usuario`, `nombre_completo`, `tipo_usuario`) VALUES
(1, 'Administrador Demo', 'ambos'),
(2, 'Player One', 'jugador');

INSERT INTO `videojuegos` (`id_usuario`, `titulo`, `descripcion`, `genero`, `plataforma`, `estado`) VALUES
(1, 'Space Invaders 2026', 'Un remake moderno del clásico de arcade.', 'Arcade', 'PC', 'terminado');

INSERT INTO `resenas` (`id_usuario`, `id_videojuego`, `calificacion`, `comentario`) VALUES
(2, 1, 5, '¡Increíble juego retro! Totalmente recomendado.');
