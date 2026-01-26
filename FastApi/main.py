# File: FastApi/main.py
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from databases import engine
import models
from router import api_router

# 1. Create Database Tables
models.Base.metadata.create_all(bind=engine)

# 2. Initialize App
app = FastAPI(
    title="Anuz User System ☄️",
    description="Professional CRUD system",
    version="1.0.0"
)

# 3. Include the Router
app.include_router(api_router)

@app.get("/", response_class=HTMLResponse, tags=["General"])
def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Anuz User System</title>
            
            <!-- BROWSER TAB LOGO (Favicon) -->
            <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>☄️</text></svg>">

            <style>
                /* RESET & LAYOUT */
                html, body {
                    height: 100%;
                    width: 100%;
                    margin: 0;
                    padding: 0;
                    overflow: hidden; /* Prevents scrolling */
                }

                body {
                    /* "Midnight Luxury" Background */
                    background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    
                    /* FORCE CENTER ALIGNMENT */
                    display: grid;
                    place-items: center;
                }

                /* THE CARD (Glassmorphism) */
                .card {
                    text-align: center;
                    padding: 80px 60px;
                    border-radius: 24px;
                    
                    /* Frosted Glass Effect */
                    background: rgba(255, 255, 255, 0.03);
                    backdrop-filter: blur(20px);
                    -webkit-backdrop-filter: blur(20px);
                    
                    /* Subtle Border & Shadow */
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
                    
                    max-width: 480px;
                    width: 90%;
                    
                    /* Smooth Entrance Animation */
                    animation: fadeUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
                    opacity: 0;
                    transform: translateY(20px);
                }

                /* TYPOGRAPHY */
                h1 {
                    font-size: 3rem;
                    margin: 0 0 16px 0;
                    color: #ffffff;
                    font-weight: 700;
                    letter-spacing: -0.02em;
                    
                    /* Subtle Gradient Text */
                    background: linear-gradient(to bottom right, #ffffff 0%, #94a3b8 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                p {
                    font-size: 1.1rem;
                    color: #94a3b8; /* Muted slate color */
                    line-height: 1.6;
                    margin-bottom: 40px;
                    font-weight: 400;
                }

                .status-dot {
                    display: inline-block;
                    width: 10px;
                    height: 10px;
                    background-color: #10b981; /* Emerald Green */
                    border-radius: 50%;
                    margin-left: 8px;
                    box-shadow: 0 0 10px #10b981;
                }

                /* THE BUTTON (Premium Look) */
                .btn {
                    display: inline-block;
                    padding: 16px 48px;
                    
                    /* "Royal Sunset" Gradient */
                    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                    
                    color: #ffffff;
                    text-decoration: none;
                    border-radius: 12px;
                    font-weight: 600;
                    font-size: 1.1rem;
                    letter-spacing: 0.5px;
                    
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }

                .btn:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 20px 25px -5px rgba(245, 158, 11, 0.3), 0 10px 10px -5px rgba(245, 158, 11, 0.2);
                    filter: brightness(1.1);
                }

                /* ANIMATION KEYFRAMES */
                @keyframes fadeUp {
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Anuz User System</h1>
                <p>
                    Secure and Fast <br>
                    System Status: Online <span class="status-dot"></span>
                </p>
                <a href="/docs" class="btn">Access Dashboard</a>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)