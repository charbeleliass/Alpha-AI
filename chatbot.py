from flask import Flask, render_template_string, request

app = Flask(__name__)


def simple_chatbot(user_query):
  query = user_query.strip()
  if query == "What is the total revenue?":
    return (
        "For FY2025, Total Revenue was: Microsoft ($281,724M), Tesla ($94,827M),"
        " Apple ($416,161M)."
    )
  elif query == "How has net income changed over the last year?":
    return (
        "Net Income (2024 to 2025): Microsoft increased by 15.54%, Tesla"
        " decreased by 46.11%, Apple increased by 19.50%."
    )
  elif query == "What is the profit margin?":
    return (
        "Profit margins for 2025: Microsoft (36.15%), Apple (26.92%), Tesla"
        " (4.07%)."
    )
  elif query == "What is the operating cash flow?":
    return (
        "Operating cash flow for 2025: Microsoft ($136,162M), Apple"
        " ($111,482M), Tesla ($14,747M)."
    )
  elif query == "How has operating cash flow changed over the last year?":
    return (
        "Operating cash flow change (2024 to 2025): Microsoft increased by"
        " 14.86%, Apple decreased by 5.73%, Tesla decreased by 1.18%."
    )
  else:
    return "Sorry, I can only provide information on predefined queries."


PAGE = """
<h2>Financial Chatbot</h2>
<form method="POST">
    <input type="text" name="query" placeholder="Ask your question here..." style="width: 300px; padding: 5px;" required>
    <button type="submit">Send</button>
</form>
{% if query %}
    <p><b>Question :</b> {{ query }}</p>
    <p><b>Réponse :</b> {{ response }}</p>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def home():
  response, query = None, None
  if request.method == "POST":
    query = request.form.get("query")
    response = simple_chatbot(query)
  return render_template_string(PAGE, query=query, response=response)


if __name__ == "__main__":
  app.run(debug=True)