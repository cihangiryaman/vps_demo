from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Statik dosyalar ve Template motoru ayarları
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# CV'den alınan veriler [cite: 1, 2, 8, 16, 21, 24, 37, 41]
profile_data = {
    "name": "Cihangir Yaman",
    "title": "Student - Backend Developer",
    "summary": "Dedicated software developer since 2018. Primary focus on .NET, also developing with Python and Java.",
    "contact": {
        "email": "cihangiryaman3200@gmail.com",
        "github": "https://github.com/cihangiryaman",
        "linkedin": "https://www.linkedin.com/in/cihangir-yaman",
        "location": "Istanbul, Turkiye"
    },
    "skills": {
        "languages": ["C#", "Python", "Java", "JavaScript", "C"],
        "frameworks": ["ASP.NET", "Entity Framework", "FastAPI", "AutoMapper", "FluentValidation"],
        "tools": ["Git", "GitHub", "MSSQL", "Redis", "Docker"]
    },
    "experience": [
        {
            "company": "NöroNest",
            "role": "Backend Team Lead (Volunteer)",
            "date": "August 2025 - Present",
            "description": "Developing ASP.NET APIs for a therapeutic game designed for Alzheimer's patients. Managing MSSQL database and backend operations."
        },
        {
            "company": "MADES (Marmara Developer Society)",
            "role": "Founder",
            "date": "October 2025 - Present",
            "description": "Founded a student club to organize conferences and trainings in software and game development."
        },
        {
            "company": "apartmanyonetimsistemi.com",
            "role": "Developer",
            "date": "July 2025 - December 2025",
            "description": "Built a multi-tenant SaaS architecture using clean architecture principles with ASP.NET and MSSQL."
        }
    ],
    "projects": [
        {
            "name": "Private Lesson Tracking System",
            "url": "https://www.ozelderstakipsistemi.com",
            "tech": "ASP.NET, MSSQL, Entity Framework",
            "desc": "A multi-tenant SaaS application enabling private tutors to track students, lessons, and payments."
        },
        {
            "name": "3D Gear CAD Generator",
            "url": "#",
            "tech": "Python, FastAPI, Redis, Three.js",
            "desc": "Generates 3D gears via gear parameters using FreeCAD API and visualizes them on the web."
        }
    ]
}

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "profile": profile_data})

if __name__ == "__main__":
    # Development ortamı için
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)