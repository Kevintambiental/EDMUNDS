# 🌍 EDMUNDS v3.0 - Sistema Profesional de Modelado de Dispersión en Suelos

Environmental Dispersion Modeling for Underground Natural Soil Systems

## 📋 Descripción

Software profesional de ingeniería para el modelado de dispersión de contaminantes en suelos, basado en el Estudio General de Suelos de Cundinamarca del IGAC (2000).

## 🚀 Cómo Desplegar en Streamlit Cloud

### Paso 1: Crear cuenta en GitHub
1. Ve a https://github.com y crea una cuenta (si no tienes)
2. Crea un nuevo repositorio llamado `edmunds`
3. Marca el repositorio como **Public**

### Paso 2: Subir archivos a GitHub
Sube estos archivos a tu repositorio de GitHub:
- `app.py`
- `requirements.txt`
- `src/` (carpeta completa)
- `.streamlit/` (carpeta completa)

### Paso 3: Crear cuenta en Streamlit Cloud
1. Ve a https://share.streamlit.io
2. Clic en "Sign up"
3. Clic en "Sign up with GitHub"
4. Autoriza Streamlit para acceder a tu GitHub

### Paso 4: Desplegar
1. En Streamlit Cloud, clic en "New app"
2. Selecciona tu repositorio `edmunds`
3. Archivo principal: `app.py`
4. Clic en "Deploy"

### Paso 5: ¡Listo!
Streamlit Cloud te dará una URL como:
- `https://edmunds-tuusuario.streamlit.app`

Esta URL funcionará en:
- ✅ PC (Windows, Mac, Linux)
- ✅ Celulares (Android, iOS)
- ✅ Tablets
- ✅ Cualquier dispositivo con navegador

## 📦 Archivos Incluidos

```
edmunds/
├── app.py                    # Aplicación principal
├── requirements.txt           # Dependencias de Python
├── src/                     # Módulos del software
│   ├── __init__.py
│   ├── cundinamarca_ucs.py    # Base de datos UCS de Cundinamarca
│   ├── contaminant_catalog.py # Catálogo de contaminantes
│   ├── transport_equations.py # Ecuaciones de transporte
│   ├── segment_modeling.py    # Modelado por tramos
│   └── plume_3d.py             # Modelado 3D
└── .streamlit/              # Configuración de Streamlit
    └── config.toml
```

## 🎯 Características

- **10 UCS de Cundinamarca** (IGAC 2000)
- **20 contaminantes** (hidrocarburos, metales, solventes, pesticidas)
- **Modelado por tramos** personalizable
- **Selección múltiple de UCS**
- **Gráficas individuales por UCS**
- **Interfaz profesional de ingeniería**

## 📚 Referencias

- Estudio General de Suelos de Cundinamarca - IGAC (2000)
- USDA Soil Texture Classification
- EPA Regional Screening Levels (RSL)
- Rawls & Brakensiek (1983)
- Cosby et al. (1984)
