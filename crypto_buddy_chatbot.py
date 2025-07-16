
# CryptoBuddy - Your Crypto Investment Sidekick

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def intro():
    print("👋 Hey there! I’m CryptoBuddy — your crypto sidekick!")
    print("I help you choose coins based on trends and sustainability 🌱📈")

def handle_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 {coin} is your best bet! It’s eco-friendly with a score of {crypto_db[coin]['sustainability_score']*10}/10.")

    elif "trending" in user_query or "rising" in user_query:
        rising_coins = [k for k, v in crypto_db.items() if v["price_trend"] == "rising"]
        print("📈 These coins are trending up: " + ", ".join(rising_coins))

    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"💡 Consider {name} — it has strong market backing and upward momentum!")
                break
        else:
            print("🔍 No coin perfectly matches that criteria right now.")

    else:
        print("❓ I didn’t get that. Try asking about 'sustainable', 'trending', or 'long-term growth'.")

def run_bot():
    intro()
    while True:
        user_query = input("\nYou: ")
        if user_query.lower() in ['exit', 'quit']:
            print("👋 See you next time! Stay green & profitable! 💸")
            break
        handle_query(user_query)

if __name__ == "__main__":
    run_bot()
