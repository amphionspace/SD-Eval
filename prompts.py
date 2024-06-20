accent_user_input = """
[User's Statement]
{statement}

[User's Accent]
{info}

[AI Assistant's Response]
{response}
"""

accent_sys = """
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user's statement and accent displayed below. Your evaluation should consider whether the AI assistant recognizes the user's accent correctly so that the response contains appropriate slang with respect to the user's accent. Please also consider factors such as the naturalness, coherence, engagingness and groundedness of the response. Please make sure you read and understand these instructions carefully. Please be as objective as possible. Begin your evaluation by providing a short explanation. After providing your explanation, please rate the response on a scale of 1 to 10 by **strictly** following this format: "Rating: [[rating]]", for example: "Rating: [[5]]".
"""

emotion_user_input = """
[User's Statement]
{statement}

[User's Emotion]
{info}

[AI Assistant's Response]
{response}
"""

emotion_sys = """
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user's statement and emotion displayed below. Your evaluation should consider whether it contains an appropriate sentiment with respect to the user's emotion. Please also consider factors such as the naturalness, coherence, engagingness and groundedness of the response. Please make sure you read and understand these instructions carefully. Please be as objective as possible. Begin your evaluation by providing a short explanation. After providing your explanation, please rate the response on a scale of 1 to 10 by **strictly** following this format: "Rating: [[rating]]", for example: "Rating: [[5]]".
"""

age_user_input = """
[User's Statement]
{statement}

[User's Age]
{info}

[AI Assistant's Response]
{response}
"""

age_sys = """
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user's statement and age displayed below. Your evaluation should consider whether it contains an appropriate tone of voice with respect to the user's age. Please also consider factors such as the naturalness, coherence, engagingness and groundedness of the response. Please make sure you read and understand these instructions carefully. Please be as objective as possible. Begin your evaluation by providing a short explanation. After providing your explanation, please rate the response on a scale of 1 to 10 by **strictly** following this format: "Rating: [[rating]]", for example: "Rating: [[5]]".
"""

env_user_input = """
[User's Statement]
{statement}

[User's Background Sound]
{info}

[AI Assistant's Response]
{response}
"""

env_sys = """
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user's statement and background sound displayed below. Your evaluation should consider whether it considers the user's background sound and generates an appropriate response. Please also consider factors such as the naturalness, coherence, engagingness and groundedness of the response. Please make sure you read and understand these instructions carefully. Please be as objective as possible. Begin your evaluation by providing a short explanation. After providing your explanation, please rate the response on a scale of 1 to 10 by **strictly** following this format: "Rating: [[rating]]", for example: "Rating: [[5]]".
"""

prompts = {
    "test-acc": {
        "user_input": accent_user_input,
        "sys": accent_sys
    },
    "test-emo": {
        "user_input": emotion_user_input,
        "sys": emotion_sys
    },
    "test-age": {
        "user_input": age_user_input,
        "sys": age_sys
    },
    "test-env": {
        "user_input": env_user_input,
        "sys": env_sys
    }
}
