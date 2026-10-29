from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    
    image_filename = "img/test/test.jpg"
    
    # Verificamos de forma segura si el archivo existe físicamente en static/
    hero_image_path = None
    if image_filename:
        full_path = os.path.join(app.static_folder, image_filename)
        if os.path.exists(full_path):
            hero_image_path = image_filename

    hero_data = {
        "title": "Hi, I'm Julie.",
        "description": "I build systems, infrastructure and intelligent solutions at the intersection of software, hardware and networks.",
        "tags": [
            "SOFTWARE ENGINEERING",
            "WEB DEVELOPMENT",
            "ANDROID DEVELOPMENT",
            "BACKEND & APIs",
            "SYSTEMS PROGRAMMING",
            "LINUX & INFRASTRUCTURE",
            "NETWORK ENGINEERING",
            "DIGITAL DESIGN",
            "AI"
            ],
        "hero_image": hero_image_path
    }

    knowledge_tools = [
        # Languages
        {"name": "Python", "icon": "</>", "category": "languages"},
        {"name": "Kotlin", "icon": "</>", "category": "languages"},
        {"name": "Java", "icon": "</>", "category": "languages"},
        {"name": "C", "icon": "</>", "category": "languages"},
        {"name": "C#", "icon": "</>", "category": "languages"},
        {"name": "JavaScript", "icon": "</>", "category": "web"},
        {"name": "HTML5", "icon": "</>", "category": "web"},
        {"name": "CSS3", "icon": "</>", "category": "web"},
        {"name": "Rust", "icon": "</>", "category": "systems"},

        # Web, backend and APIs
        {"name": "Flask", "icon": "Fl", "category": "backend"},
        {"name": "FastAPI", "icon": "API", "category": "backend"},
        {"name": "REST APIs", "icon": "{ }", "category": "backend"},

        # Data formats
        {"name": "JSON", "icon": "{ }", "category": "data-formats"},
        {"name": "CSV", "icon": "CSV", "category": "data-formats"},

        # Databases and persistence
        {"name": "SQLite", "icon": "SQL", "category": "data"},
        {"name": "MySQL", "icon": "SQL", "category": "data"},
        {"name": "MongoDB", "icon": "DB", "category": "data"},
        {"name": "Redis", "icon": "R", "category": "data"},

        # Android
        {"name": "Android", "icon": "An", "category": "mobile"},
        {"name": "Jetpack Compose", "icon": "JC", "category": "mobile"},
        {"name": "Room", "icon": "DB", "category": "mobile"},
        {"name": "DataStore", "icon": "KV", "category": "mobile"},

        # AI and scientific computing
        {"name": "Ollama", "icon": "AI", "category": "ai"},
        {"name": "Hugging Face", "icon": "HF", "category": "ai"},
        {"name": "Qdrant", "icon": "Q", "category": "ai"},
        {"name": "NumPy", "icon": "np", "category": "ai"},
        {"name": "Pandas", "icon": "pd", "category": "ai"},

        # Infrastructure
        {"name": "Tailscale", "icon": "~", "category": "infrastructure"},
        {"name": "SSH", "icon": ">_", "category": "infrastructure"},

        # Systems and development tools
        {"name": "VS Code", "icon": "</>", "category": "tools"},
        {"name": "Android Studio", "icon": "AS", "category": "tools"},
        {"name": "Linux", "icon": "$_", "category": "systems"},
        {"name": "Git", "icon": "Gt", "category": "tools"},
        {"name": "GitHub", "icon": "GH", "category": "tools"},
        {"name": "Docker", "icon": "[]", "category": "tools"},

        # Digital design and hardware
        {"name": "Logisim", "icon": "CPU", "category": "hardware"},
        {"name": "Assembler", "icon": "0x", "category": "hardware"},
        {"name": "Raspberry Pi", "icon": "π", "category": "hardware"},
    ]

    featured_projects = [
        {
            "name": "Noir Assistant",
            "description": "AI assistant with OCR, RAG and tools.",
            "icon": "⌁", # O etiquetas SVG directas
            "href": "#projects"
        },
        {
            "name": "Homelab Platform",
            "description": "Self-hosted infrastructure and services.",
            "icon": "⌂",
            "href": "#projects"
        },
        {
            "name": "AI Local Stack",
            "description": "Ollama, embeddings, local inference.",
            "icon": "⚙",
            "href": "#projects"
        },
        {
            "name": "IoT Automation",
            "description": "Smart home, sensors and automations.",
            "icon": "❖",
            "href": "#projects"
        }
    ]

    projects = [
        {
            "id": "01",
            "total": "04",
            "name": "Milo ISA",
            "description": "Una tarjeta visual con descripción, tecnologías y enlace al proyecto.",
            "image": "img/test/test0.jpg",
            "techs": "Hardware / C / RISC",
            "href": "#projects"
        },
        {
            "id": "02",
            "total": "04",
            "name": "Homelab Platform",
            "description": "Infraestructura autohospedada, redes y servicios privados.",
            "image": "img/test/test1.jpg",
            "techs": "Linux / Docker / Tailscale",
            "href": "#projects"
        },
        {
            "id": "03",
            "total": "04",
            "name": "Local AI Inference",
            "description": "Experimentación con modelos locales e integración de herramientas.",
            "image": "img/test/test2.jpg",
            "techs": "Python / PyTorch / Ollama",
            "href": "#projects"
        },
        {
            "id": "04",
            "total": "04",
            "name": "IoT & Automation",
            "description": "Dispositivos conectados, sensores y automatización de procesos.",
            "image": "img/test/test3.jpg",
            "techs": "Embedded / MQTT / Rust",
            "href": "#projects"
        }
    ]

    return render_template(
        "index.html",
        hero=hero_data,
        knowledge_tools=knowledge_tools,
        featured_projects=featured_projects,
        projects=projects,
        year=datetime.now().year,
    )

@app.route("/old")
def old():
    # Datos de ejemplo para la interfaz. Más adelante se pueden mover a JSON
    # o conectar con servicios reales del homelab.
    status = {
        "lab_uptime": "—",
        "devices_online": "1 online / 1 planned",
        "services_running": "—",
        "tailscale": "private network",
        "internet": "not monitored",
    }

    projects = [
        {
            "icon": "◈",
            "name": "Milo ISA",
            "description": "Experimental CPU architecture and instruction set.",
            "tag": "hardware",
            "href": "#projects",
        },
        {
            "icon": "⌘",
            "name": "Homelab Platform",
            "description": "Self-hosted infrastructure, networking and services.",
            "tag": "infrastructure",
            "href": "#lab",
        },
        {
            "icon": "✳",
            "name": "Local AI",
            "description": "Experiments with local inference and intelligent tools.",
            "tag": "ai",
            "href": "#projects",
        },
        {
            "icon": "⌁",
            "name": "IoT & Automation",
            "description": "Connected devices, sensors and automation ideas.",
            "tag": "embedded",
            "href": "#knowledge",
        },
    ]

    notes = [
        {"title": "Building my personal homelab", "tag": "infrastructure", "date": "draft"},
        {"title": "Tailscale, HTTPS and reverse proxies", "tag": "networking", "date": "draft"},
        {"title": "Exploring CPU architecture with an ISA", "tag": "hardware", "date": "draft"},
        {"title": "Running local AI workloads", "tag": "ai", "date": "draft"},
    ]

    skills = [
        {"name": "AI / ML", "x": 50, "y": 8},
        {"name": "Linux", "x": 83, "y": 22},
        {"name": "Networking", "x": 88, "y": 55},
        {"name": "FPGA", "x": 72, "y": 85},
        {"name": "Automation", "x": 28, "y": 85},
        {"name": "Security", "x": 12, "y": 55},
        {"name": "Embedded", "x": 17, "y": 22},
    ]

    return render_template(
        "old.html",
        status=status,
        projects=projects,
        notes=notes,
        skills=skills,
        year=datetime.now().year,
    )

if __name__ == "__main__":
    app.run(debug=True)