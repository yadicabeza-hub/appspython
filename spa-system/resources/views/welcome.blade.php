<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{{ config('app.name', 'AppsPython SPA') }}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
        <div id="app" class="min-h-screen flex flex-col">
            <!-- Navbar -->
            <nav class="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-50">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between items-center h-16">
                        <div class="flex items-center">
                            <h1 class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                                AppsPython
                            </h1>
                        </div>
                        <div class="flex items-center space-x-6">
                            @auth
                                <a href="{{ url('/dashboard') }}" class="text-gray-700 dark:text-gray-300 hover:text-blue-600 transition">
                                    Dashboard
                                </a>
                            @else
                                <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-blue-600 transition">
                                    Login
                                </a>
                                <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-purple-600 transition">
                                    Register
                                </a>
                            @endauth
                        </div>
                    </div>
                </div>
            </nav>

            <!-- Hero Section -->
            <div class="flex-1 flex items-center justify-center px-4 py-20">
                <div class="text-center max-w-2xl">
                    <div class="mb-8">
                        <h2 class="text-5xl md:text-6xl font-bold mb-6 text-gray-900 dark:text-white">
                            Bienvenido a <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">AppsPython</span>
                        </h2>
                        <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-400 mb-4">
                            Tu plataforma SPA con Laravel y Vite
                        </p>
                        <p class="text-gray-500 dark:text-gray-500">
                            Una aplicación moderna construida con las mejores prácticas de desarrollo web
                        </p>
                    </div>

                    @guest
                        <div class="flex flex-col sm:flex-row gap-4 justify-center mt-10">
                            <a href="#" class="px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition shadow-lg hover:shadow-xl">
                                Iniciar Sesión
                            </a>
                            <a href="#" class="px-8 py-3 bg-purple-600 text-white font-semibold rounded-lg hover:bg-purple-700 transition shadow-lg hover:shadow-xl">
                                Registrarse
                            </a>
                        </div>
                    @else
                        <div class="mt-10">
                            <a href="{{ url('/dashboard') }}" class="px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition shadow-lg hover:shadow-xl inline-block">
                                Ir al Dashboard
                            </a>
                        </div>
                    @endguest

                    <div class="mt-16 pt-12 border-t border-gray-200 dark:border-gray-700">
                        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-6">Características</h3>
                        <div class="grid md:grid-cols-3 gap-8">
                            <div class="p-6 bg-white dark:bg-gray-800 rounded-lg shadow">
                                <div class="text-3xl mb-2">🚀</div>
                                <h4 class="font-semibold text-gray-900 dark:text-white mb-2">Rápido</h4>
                                <p class="text-gray-600 dark:text-gray-400 text-sm">Construido con Vite para rendimiento máximo</p>
                            </div>
                            <div class="p-6 bg-white dark:bg-gray-800 rounded-lg shadow">
                                <div class="text-3xl mb-2">🔒</div>
                                <h4 class="font-semibold text-gray-900 dark:text-white mb-2">Seguro</h4>
                                <p class="text-gray-600 dark:text-gray-400 text-sm">Autenticación segura con Laravel</p>
                            </div>
                            <div class="p-6 bg-white dark:bg-gray-800 rounded-lg shadow">
                                <div class="text-3xl mb-2">🎨</div>
                                <h4 class="font-semibold text-gray-900 dark:text-white mb-2">Moderno</h4>
                                <p class="text-gray-600 dark:text-gray-400 text-sm">Diseño responsivo con Tailwind CSS</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <footer class="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 py-6">
                <div class="max-w-7xl mx-auto px-4 text-center text-gray-600 dark:text-gray-400 text-sm">
                    <p>&copy; 2026 AppsPython. Todos los derechos reservados.</p>
                </div>
            </footer>
        </div>
    </body>
</html>
