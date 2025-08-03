## Main Experiment Prompts

### System Prompt (Persona-Based)
```
You are answering questions as if you were a human. Do not break character. You are a {{ agent.age }} year old {{ agent.gender_text }} who is {{ agent.marital_text }} with an education level of {{ agent.education }} degree and income category of {{ agent.income }} who lives in {{ agent.state }}.
```

### Probability Distribution Question (Pre-Treatment)
```
Please estimate the probability (as a percentage) for each of the following inflation/deflation scenarios over the next 12 months.

Each probability must be between 0% and 100%.
You may use up to 2 decimal points (e.g., 7.25%).
The sum of all probabilities must equal exactly 100%.
Return only a list of the numbers (i.e., 50 instead of '50%').

• Deflation of 12% or more: _____%
• Deflation between 8% and 12%: _____%
• Deflation between 4% and 8%: _____%
• Deflation between 2% and 4%: _____%
• Deflation between 0% and 2%: _____%
• Inflation between 0% and 2%: _____%
• Inflation between 2% and 4%: _____%
• Inflation between 4% and 8%: _____%
• Inflation between 8% and 12%: _____%
• Inflation of 12% or more: _____%

Please respond with a dictionary using the following keys: inflation_forecast.

Do not include "python" for create a code block. Just return the dictionary.
Here are descriptions of the values to provide:
- "inflation_forecast": "List of probability percentages for different inflation/deflation scenarios, must sum to 100"
The values should be formatted in the following types: "inflation_forecast": "list"
If you do not have a value for a given key, use "null".
After the answer, you can put a comment explaining your response on the next line.
```

### Point Prediction Question (Post-Treatment)
```
Consider the following current event: {{ info }}
What do you expect the rate of inflation to be over the next 12 months? Please give your best guess.
```
