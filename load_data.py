from django.contrib.auth.models import User
from core.models import Question, Answer
from datetime import datetime
from random import randint

# Replace with your superuser or create a default user
user = User.objects.filter(username='admin').first()
if not user:
    user = User.objects.create_user(username='admin', password='admin123')

qna_data = [
    ("What is the share market?", "It's a place where people buy and sell shares of public companies to invest and grow money."),
    ("Is it safe to invest in the stock market?", "Yes, if you invest wisely and for the long term. Avoid gambling or chasing quick profits."),
    ("Can beginners invest in stocks?", "Absolutely! Start with index funds or blue-chip stocks via apps like Zerodha or Groww."),
    ("What are blue-chip stocks?", "Stocks of well-established, financially sound companies like TCS, Infosys, or HDFC."),
    ("How much money do I need to start investing?", "Even ₹100 is enough to start with mutual funds or fractional shares."),
    ("What is an IPO?", "Initial Public Offering – when a private company first sells its shares to the public."),
    ("Best way to learn stock market?", "Watch YouTube, read books like The Intelligent Investor, and use practice apps like Moneybhai."),

    ("Is Chennai expensive to live in?", "Compared to Bangalore or Mumbai, it’s more affordable."),
    ("Best areas to live in Chennai?", "Velachery, Anna Nagar, OMR, and Adyar are popular."),
    ("Is Chennai good for IT jobs?", "Yes, it's a major IT hub with TCS, Infosys, Accenture, and Zoho."),
    ("How’s the weather in Chennai?", "Hot and humid most of the year, with rains from October to December."),
    ("Does Chennai have good public transport?", "Yes! Metro rail, buses, and suburban trains are available."),
    ("Is Chennai safe for women?", "Relatively safe in well-lit areas; avoid deserted spots at night."),
    ("Famous food in Chennai?", "Idli, dosa, filter coffee, and biryani from Dindigul Thalappakatti."),

    ("How does Tamil Nadu rank in India’s economy?", "It's among the top 3 state economies in India."),
    ("What drives Tamil Nadu’s economy?", "Manufacturing, automobiles, textiles, IT, and agriculture."),
    ("Which city in Tamil Nadu is best for business?", "Chennai leads, followed by Coimbatore and Madurai."),
    ("Does Tamil Nadu have good infrastructure?", "Yes, with ports, metro, highways, and industrial zones."),
    ("How much does Tamil Nadu contribute to India’s GDP?", "Around 8–9% of India’s GDP."),
    ("Is Tamil Nadu good for startups?", "Yes! Chennai and Coimbatore are emerging startup hubs."),
    ("What’s the literacy rate in Tamil Nadu?", "Around 82%, higher than the national average."),
]

for q_text, a_text in qna_data:
    question = Question.objects.create(user=user, title=q_text, created_at=datetime.now())
    Answer.objects.create(question=question, user=user, text=a_text, created_at=datetime.now())

print("✅ Sample Q&A inserted successfully!")