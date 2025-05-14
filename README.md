Microservicios Brazzino666 🎲
Descripción 📝
Este repositorio contiene un sistema de microservicios para una plataforma de casino, desarrollado con Django y Django REST Framework. Incluye módulos independientes para gestión de cuentas y verificación KYC .

Servicios Implementados 🛠️
1. Microservicio de Cuentas
Creación y gestión de cuentas de usuario
Consulta de saldos y estados
Actualización de información
2. Microservicio KYC
Verificación de identidad de usuarios
Gestión de documentos (identificación, comprobantes)
Flujos de aprobación/rechazo

Tecnologías Utilizadas 💻
Backend: Django 5.2 + Django REST Framework

Base de Datos: mysql

Configuración Inicial ⚙️
Clonar repositorio:
git clone https://github.com/AdrianJimenezAduaeasy/Brazziono666.git
cd Brazziono666
Configurar entorno virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Ejecución 🚀
# Microservicio de usuarios y pagos
python manage.py runserver
# Microservicio de cuentas y reportes
cd microservicio_cuentas
python manage.py runserver 8000

# Microservicio KYC (en otra terminal)
cd microservicio_kyc
python manage.py runserver 8001
