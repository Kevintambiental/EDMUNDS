# 🌍 EDMUNDS v3.0 - Sistema Profesional de Modelado de Dispersión en Suelos

Environmental Dispersion Modeling for Underground Natural Soil Systems

## 📋 Descripción

Software profesional de ingeniería para el modelado de dispersión de contaminantes en suelos, basado en el Estudio General de Suelos de Cundinamarca del IGAC (2000).

## 🌐 Sitio web independiente

La versión autónoma de EDMUNDS está publicada en [GitHub Pages](https://kevintambiental.github.io/EDMUNDS/) desde `index.html`. Esta página es independiente de la aplicación Python descrita abajo.

## 🚀 Cómo desplegar la aplicación Python en Streamlit Cloud

El repositorio público `Kevintambiental/EDMUNDS` ya existe y contiene el código Python. No es necesario crear otro repositorio ni volver a subir los archivos.

### Paso 1: Crear cuenta en Streamlit Cloud
1. Ve a https://share.streamlit.io
2. Clic en "Sign up"
3. Clic en "Sign up with GitHub"
4. Autoriza Streamlit para acceder a tu GitHub

### Paso 2: Desplegar
1. En Streamlit Cloud, clic en "New app"
2. Selecciona el repositorio `Kevintambiental/EDMUNDS`
3. Archivo principal: `app.py`
4. Clic en "Deploy"

### Paso 3: ¡Listo!
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
