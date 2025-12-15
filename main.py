from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Statik dosyalar ve Template motoru ayarları
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# CV'den alınan veriler
profile_data = {
    "name": "Cihangir Yaman",
    "title": "Student - Backend Developer",
    "tagline": "Building robust backend solutions since 2018",
    "summary": "Dedicated software developer since 2018 with a primary focus on .NET development. Experienced in building scalable backend systems, SaaS applications, and API development. Also proficient in Python and Java. Passionate about clean architecture, software design patterns, and leading development teams.",
    "contact": {
        "email": "cihangiryaman3200@gmail.com",
        "github": "https://github.com/cihangiryaman",
        "linkedin": "https://www.linkedin.com/in/cihangir-yaman",
        "location": "Istanbul, Turkiye",
        "phone": "+90 (552) 123 4567"
    },
    "education": {
        "degree": "Bachelor's Degree in Computer Engineering",
        "university": "Marmara University",
        "date": "2023 - Present",
        "gpa": "3.67/4.00"
    },
    "skills": {
        "languages": ["C#", "Python", "Java", "JavaScript", "C", "SQL"],
        "frameworks": ["ASP.NET Core", "Entity Framework", "FastAPI", "AutoMapper", "FluentValidation", "MediatR"],
        "tools": ["Git", "GitHub", "MSSQL", "Redis", "Docker", "Visual Studio", "Rider"],
        "concepts": ["Clean Architecture", "CQRS", "Repository Pattern", "Multi-Tenant SaaS", "RESTful APIs", "Microservices"]
    },
    "experience": [
        {
            "company": "NöroNest",
            "role": "Backend Team Lead (Volunteer)",
            "date": "August 2025 - Present",
            "location": "Remote",
            "description": "Leading the backend development team for a therapeutic game designed for Alzheimer's patients. Developing ASP.NET Core APIs and managing MSSQL database operations.",
            "highlights": [
                "Leading a team of backend developers",
                "Architecting scalable API solutions",
                "Managing database design and optimization",
                "Implementing secure authentication systems"
            ]
        },
        {
            "company": "MADES (Marmara Developer Society)",
            "role": "Founder & President",
            "date": "October 2025 - Present",
            "location": "Istanbul, Turkiye",
            "description": "Founded and leading a student club focused on organizing conferences, workshops, and training sessions in software and game development.",
            "highlights": [
                "Established club from ground up",
                "Organizing technical workshops and seminars",
                "Building a community of developers",
                "Coordinating with industry professionals"
            ]
        },
        {
            "company": "apartmanyonetimsistemi.com",
            "role": "Full Stack Developer",
            "date": "July 2025 - December 2025",
            "location": "Remote",
            "description": "Developed a comprehensive multi-tenant SaaS apartment management system using clean architecture principles with ASP.NET Core and MSSQL.",
            "highlights": [
                "Implemented multi-tenant SaaS architecture",
                "Applied clean architecture and CQRS patterns",
                "Developed RESTful APIs with ASP.NET Core",
                "Managed database design and migrations"
            ]
        }
    ],
    "projects": [
        {
            "name": "Private Lesson Tracking System",
            "url": "https://www.ozelderstakipsistemi.com",
            "tech": ["ASP.NET Core", "MSSQL", "Entity Framework", "Clean Architecture"],
            "desc": "A comprehensive multi-tenant SaaS application enabling private tutors to efficiently track students, schedule lessons, manage payments, and generate reports. Features include automated notifications, calendar integration, and financial analytics.",
            "featured": True,
            "github": None
        },
        {
            "name": "3D Gear CAD Generator",
            "url": None,
            "tech": ["Python", "FastAPI", "Redis", "Three.js", "FreeCAD API"],
            "desc": "An innovative web application that generates 3D gear models based on user-defined parameters using the FreeCAD API. Features real-time 3D visualization in the browser using Three.js and caching with Redis for improved performance.",
            "featured": True,
            "github": None
        },
        {
            "name": "Apartment Management System",
            "url": None,
            "tech": ["ASP.NET Core", "MSSQL", "Clean Architecture", "CQRS"],
            "desc": "Multi-tenant SaaS platform for apartment management with features including expense tracking, payment collection, announcement systems, and resident communication tools.",
            "featured": False,
            "github": None
        }
    ],
    "certifications": [
        {
            "name": "Software Testing with Copilot",
            "issuer": "LinkedIn Learning",
            "date": "November 2024"
        },
        {
            "name": "Advanced C# Fundamentals",
            "issuer": "BTK Academy",
            "date": "November 2023"
        }
    ],
    "languages": [
        {"name": "Turkish", "level": "Native"},
        {"name": "English", "level": "Professional Working Proficiency"}
    ]
}

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "profile": profile_data})

if __name__ == "__main__":
    # Development ortamı için
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)