from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Business Assistant API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ai-business-assistant-sigma.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BusinessInfo(BaseModel):
    businessName: str
    businessType: str
    offer: str
    targetCustomers: str
    location: str


@app.get("/")
def root():
    return {
        "message": "AI Business Assistant API is running!"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/api/business")
def create_business(business: BusinessInfo):
    return {
        "message": f"Business information received for {business.businessName}!",
        "business": business.model_dump()
    }


@app.post("/api/generate")
def generate_content(business: BusinessInfo):

    name = business.businessName
    business_type = business.businessType
    offer = business.offer
    customers = business.targetCustomers
    location = business.location

    social_media = (
        f"✨ Discover {name} — your local {business_type} in {location}!\n\n"
        f"We offer {offer}.\n"
        f"Perfect for {customers}.\n\n"
        f"Visit {name} today and experience the difference! 🚀"
    )

    marketing_email = (
        f"Subject: Discover {name} today! 🎉\n\n"
        f"Hello,\n\n"
        f"Looking for great {business_type.lower()} services in {location}?\n\n"
        f"{name} offers {offer}, specially designed for {customers}.\n\n"
        f"Get in touch with us today!\n\n"
        f"Best regards,\n{name}"
    )

    product_description = (
        f"{name} provides high-quality {offer}. "
        f"Our services are designed especially for {customers} "
        f"in {location}. We focus on quality, value and customer satisfaction."
    )

    business_ideas = [
        f"Create a special offer for {customers}.",
        f"Post weekly content highlighting {offer}.",
        f"Launch a referral program for existing customers.",
        f"Create location-based promotions for customers in {location}.",
        f"Share customer testimonials on social media."
    ]

    return {
        "success": True,
        "message": "Content generated successfully!",
        "socialMedia": social_media,
        "marketingEmail": marketing_email,
        "productDescription": product_description,
        "businessIdeas": business_ideas,
        "content": {
            "socialMedia": social_media,
            "marketingEmail": marketing_email,
            "productDescription": product_description,
            "businessIdeas": business_ideas
        }
    }