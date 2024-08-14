import os
import openai

openai.api_key = "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"

def get_pitch_deck_guidance():
    prompt = """
    Provide templates and examples of successful pitch decks. Offer tips on structuring the pitch and highlighting key points.
    """
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def get_vc_questions_and_answers():
    prompt = """
    Compile a list of common questions VCs ask and provide model answers. Offer advice on how to handle difficult or unexpected questions.
    """
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def get_vc_matching(industry, stage, location):
    prompt = f"""
    Suggest potential VCs based on the startup's industry: {industry}, stage: {stage}, and location: {location}.
    Provide information on the investment preferences and track records of suggested VCs.
    """
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def get_vc_concepts_and_strategies():
    prompt = """
    Explain key VC concepts such as equity, valuation, ROI, and term sheets. Summarize insights from popular VC podcasts and investment memos.
    """
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def get_fundraising_strategy_feedback(strategy_description):
    prompt = f"""
    Analyze the founder's current fundraising strategy: {strategy_description} and provide feedback. Suggest improvements based on best practices and successful case studies.
    """
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def simulate_vc_conversation(user_input):
    prompt = f"""
    Simulate a VC conversation. The user asked: "{user_input}". Provide feedback on the user's questions and suggest improvements.
    """
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def main():
    print("VC Bot: How can I assist you today? I am happy to answer questions regarding pitch deck guidance, VC Q&A, VC matching, VC concepts/strategies, fundraising, and simulating VC conversations.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ['exit', 'quit']:
            print("VC Bot: Goodbye!")
            break
        elif "pitch deck guidance" in user_input:
            response = get_pitch_deck_guidance()
        elif "vc questions and answers" in user_input:
            response = get_vc_questions_and_answers()
        elif "vc matching" in user_input:
            industry = input("Enter industry: ")
            stage = input("Enter stage: ")
            location = input("Enter location: ")
            response = get_vc_matching(industry, stage, location)
        elif "vc concepts and strategies" in user_input:
            response = get_vc_concepts_and_strategies()
        elif "fundraising strategy feedback" in user_input:
            strategy_description = input("Describe your fundraising strategy: ")
            response = get_fundraising_strategy_feedback(strategy_description)
        elif "simulate vc conversation" in user_input:
            user_query = input("Enter your question: ")
            response = simulate_vc_conversation(user_query)
        else:
            response = "I'm sorry, I didn't understand that. Can you please specify one of the following: pitch deck guidance, VC questions and answers, VC matching, VC concepts and strategies, fundraising strategy feedback, or simulate VC conversation."

        print(f"VC Bot: {response}")

if __name__ == "__main__":
    main()









