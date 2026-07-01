# 🚀 FastAPI Lab: Dominando la Creación de APIs en Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-brightgreen)](https://github.com/Astharmin/Python_FastAPI)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow)](LICENSE)

## 📖 ¿Qué es este proyecto?

Este repositorio es mi **cuaderno de prácticas y laboratorio personal** para dominar el desarrollo de APIs robustas y de alto rendimiento con **FastAPI** y el ecosistema de Python.

No es un simple tutorial, sino un lugar donde **construyo, pruebo y documento** cada concepto, desde los fundamentos hasta las técnicas más avanzadas. Cada archivo y módulo representa una lección aprendida, un error superado o un patrón de diseño dominado.

El objetivo es convertir este conocimiento en un conjunto de recetas y componentes reutilizables que pueda aplicar en proyectos reales.

> *"De la teoría a la práctica, una API a la vez."*

---

## 🗺️ Hoja de Ruta de Aprendizaje (Módulos)

El contenido está organizado en módulos que cubren todo el espectro del desarrollo con FastAPI. A medida que avanzo, los iré completando y actualizando.

| Módulo | Estado | Descripción |
| :--- | :--- | :--- |
| **1. 🧱 Fundamentos y primeros pasos** | ✅ **Completado** | Configuración inicial, rutas básicas, métodos HTTP (GET, POST, PUT, DELETE), y el poder de la documentación automática con Swagger UI. |
| **2. 📦 Gestión de Datos y Validación** | ✅ **Completado** | Uso de **Pydantic** para la validación de datos, creación de esquemas, manejo de diferentes tipos de datos y respuestas personalizadas. |
| **3. 🗄️ Integración con Bases de Datos** | ✅ **Completado** | Conexión con bases de datos SQL (SQLAlchemy, Alembic) y NoSQL (MongoDB), creación de CRUDs completos y manejo de transacciones. |
| **4. 👤 Autenticación y Autorización** | 🔜 **Próximamente** | Implementación de seguridad con **OAuth2**, manejo de JWT (JSON Web Tokens), protección de rutas y gestión de usuarios y permisos. |
| **5. 📁 Archivos y Recursos** | 🔜 **Próximamente** | Subida y descarga de archivos, manejo de imágenes y otros recursos estáticos. |
| **6. 🧩 Estructura Avanzada** | 🔜 **Próximamente** | Organización de proyectos a gran escala con **Dependencias**, **APIRouter** para versionado y modularización. |
| **7. 📊 Extracción de Datos (Web Scraping)** | 🔜 **Próximamente** | Creación de APIs que actúan como puente entre datos externos (scraping) y el usuario final. |
| **8. 🕒 Tareas Asíncronas y en Segundo Plano** | 🔜 **Próximamente** | Uso de **Celery** y Redis para manejar tareas de larga duración sin bloquear la API, mejorando el rendimiento y la experiencia de usuario. |
| **9. 🚀 Orquestación con Docker** | 🔜 **Próximamente** | Creación de contenedores Docker para la API y sus dependencias, y orquestación de múltiples servicios (API, DB, Redis, Celery) con Docker Compose. |
| **10. 📡 WebSockets** | 🔜 **Próximamente** | Implementación de comunicación en tiempo real para funcionalidades como chats, notificaciones o actualizaciones en vivo. |
| **11. 🧪 Testing y Calidad** | 🔜 **Próximamente** | Escritura de pruebas unitarias y de integración con **Pytest** para asegurar la robustez y fiabilidad de la API. |

---

## 🚀 Cómo empezar

1.  **Clona el repositorio**:
    ```bash
    git clone https://github.com/Astharmin/Python_FastAPI.git
    cd Python_FastAPI
    ```

2.  **Configura un entorno virtual** (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias base**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación**:
    ```bash
    uvicorn app.main:app --reload
    ```

5.  **Explora la documentación interactiva** en `http://127.0.0.1:8000/docs`.

---

## ✨ Tecnologías Clave

Este laboratorio se construye sobre un ecosistema moderno y potente de Python:

*   **[FastAPI](https://fastapi.tiangolo.com/):** El framework principal para construir la API.
*   **[Pydantic](https://docs.pydantic.dev/):** Para la validación y serialización de datos.
*   **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para la interacción con bases de datos SQL.
*   **[Alembic](https://alembic.sqlalchemy.org/):** Para el versionado y manejo de migraciones de la base de datos.
*   **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI de alto rendimiento para ejecutar FastAPI.
*   **[Docker](https://www.docker.com/):** Para empaquetar y desplegar la aplicación y sus dependencias.

## 🙌 Contribuciones

Este es un proyecto de aprendizaje personal, pero si encuentras un bug, tienes una sugerencia o quieres compartir una mejora, ¡será bienvenida! Siéntete libre de abrir un **issue** o un **pull request**.

---

## 🧾 Licencia

MIT — ¡aprende, usa y comparte libremente!

---

⭐ **Si este laboratorio te sirve de inspiración, dale una estrella para seguir su evolución.** ⭐

---