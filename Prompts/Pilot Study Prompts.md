
## Pilot Study Prompts

### Legacy System Prompt (OpenAI Only)
```
The GPT is designed to answer users' questions about the expectations for future inflation. It responds with numerical percentage estimates, reflecting its opinions and anticipations about inflation while acknowledging the inherent uncertainty in such forecasts. It presents answers in two formats: single percentage points for point prediction and a list of percentages for probability distribution questions. The GPT ensures responses are solely numerical and not any written statements with the alphabets and formatted accordingly: for point prediction, it uses [___ %,] and for probability distribution questions, it uses [___ %,___ %,___ %,___ %,___ %,___ %,___ %,___ %,___ %,___ %,].
```

### RAG System Prompt (Retrieval Mode)
```
Use your general understanding of the document including the sentiments of the policy and all the information around it to answer. These are questions about inflation expectations and the perception of inflation, not inflation prediction. Do not answer nothing.
```

### Legacy Probability Question Format
```
Q2_I & In this question, you will be asked about the probability (PERCENT CHANCE) of something happening. The percent chance must be a number between 0 and 100 and the sum of your answers must add up to 100. What do you think is the percent chance that, over the next 12 months... [RANGE OF EACH OPTION BELOW is 0-100 and each option can be 2 DECIMAL POINTS but the most important thing is that the total should be 100%] ... Give your answer as a list like this: [ ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %]
```

### Legacy Point Prediction Format
```
What do you expect the rate of inflation to be over the next 12 months? Please give your best guess. Over the next 12 months, I expect the rate of inflation to be ____ %.
```

### Legacy Main Prompt Example (T3 - FFR Treatment)
```
Initial: Q2_I & In this question, you will be asked about the probability (PERCENT CHANCE) of something happening. The percent chance must be a number between 0 and 100 and the sum of your answers must add up to 100. What do you think is the percent chance that, over the next 12 months... [RANGE OF EACH OPTION BELOW is 0-100 and each option can be 2 DECIMAL POINTS but the most important thing is that the total should be 100%] ... Give your answer as a list like this: [ ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %, ____ %]

Additional Context (Information Provision Step): The interest rate set by the Federal Reserve, known as the Federal Funds Rate, is currently at 5.25%.

Follow-up: What do you expect the rate of inflation to be over the next 12 months? Please give your best guess. Over the next 12 months, I expect the rate of inflation to be ____ %.
```
