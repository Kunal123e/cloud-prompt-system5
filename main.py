from flask import Flask, render_template, request

app = Flask(__name__)


def process_prompt(prompt):
    if not prompt:
        return "Please enter a prompt."

    prompt = prompt.lower()

    if "explain cloud computing" in prompt:
        return "Cloud computing is the delivery of computing services like storage, servers, and software over the internet."

    elif "generate project ideas" in prompt:
        return """Here are some project ideas:
1. Cloud File Storage System
2. Online Attendance System
3. E-Learning Platform
4. Weather Information App"""

    elif "summarize" in prompt:
        text = prompt.replace("summarize this text:", "")
        sentences = text.strip().split(".")
        return "Summary: " + sentences[0] if sentences[0] else "Please provide text to summarize."

    elif "hello" in prompt or "hi" in prompt:
        return "Hello! Welcome to the Cloud-Based Prompt System."

    else:
        return "Sorry, I cannot understand your prompt."


@app.route("/", methods=["GET", "POST"])
def home():
    user_prompt = ""
    response = ""

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "")
        response = process_prompt(user_prompt)

    return render_template("index.html",
                           response=response,
                           user_prompt=user_prompt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
