# Financial Loss Extraction: "Lost Wealth" Example

LangExtract can be used to extract structured financial information from documents, including details about financial losses, investments, and wealth changes. This example demonstrates extracting "lost wealth" information from financial narratives.

> **Disclaimer:** This demonstration is for illustrative purposes only. It does not constitute financial advice and should not be used for making investment decisions.

---

## Basic Financial Loss Extraction

This example shows how to extract structured information about financial losses from text:

```python
import langextract as lx

# Define the extraction prompt
prompt_description = """Extract financial loss information including:
- Loss events (what was lost)
- Loss amounts (monetary values)
- Loss causes (why the loss occurred)
- Time periods (when the loss happened)
- Affected entities (who experienced the loss)

Use exact text for extractions. Do not paraphrase or overlap entities.
Provide meaningful attributes for each entity to add context."""

# Provide a high-quality example to guide the model
examples = [
    lx.data.ExampleData(
        text="The company reported a $2.5 million loss in Q3 2023 due to market volatility and poor investment decisions.",
        extractions=[
            lx.data.Extraction(
                extraction_class="affected_entity",
                extraction_text="The company",
                attributes={"type": "organization"}
            ),
            lx.data.Extraction(
                extraction_class="loss_amount",
                extraction_text="$2.5 million loss",
                attributes={"currency": "USD", "value": "2500000"}
            ),
            lx.data.Extraction(
                extraction_class="time_period",
                extraction_text="Q3 2023",
                attributes={"quarter": "Q3", "year": "2023"}
            ),
            lx.data.Extraction(
                extraction_class="loss_cause",
                extraction_text="market volatility",
                attributes={"category": "market_conditions"}
            ),
            lx.data.Extraction(
                extraction_class="loss_cause",
                extraction_text="poor investment decisions",
                attributes={"category": "management_decisions"}
            )
        ]
    )
]

# Input text to process
input_text = """John Smith lost $50,000 in the stock market crash of 2024. 
The losses were primarily from tech stocks that declined sharply in March."""

# Run the extraction
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt_description,
    examples=examples,
    model_id="gemini-2.5-flash",
)

# Display results
print(f"Found {len(result.extractions)} financial loss entities")
for extraction in result.extractions:
    print(f"  - {extraction.extraction_class}: {extraction.extraction_text}")
    if extraction.attributes:
        print(f"    Attributes: {extraction.attributes}")
```

## Expected Output

The extraction should identify:
- **Affected entity**: "John Smith" (type: individual)
- **Loss amount**: "$50,000" (currency: USD, value: 50000)
- **Loss event**: "stock market crash of 2024" (type: market_event)
- **Time period**: "2024" (year: 2024), "March" (month: March)
- **Loss cause**: "tech stocks that declined sharply" (category: asset_depreciation)

## Visualization

Like other LangExtract examples, you can save and visualize the results:

```python
# Save results to JSONL
lx.io.save_annotated_documents([result], output_name="financial_losses.jsonl", output_dir=".")

# Generate interactive HTML visualization
html_content = lx.visualize("financial_losses.jsonl")
with open("financial_losses_viz.html", "w") as f:
    if hasattr(html_content, 'data'):
        f.write(html_content.data)
    else:
        f.write(html_content)
```

## Advanced Use Case: Portfolio Loss Analysis

For more complex financial documents, you can extract detailed portfolio losses:

```python
# More detailed example for portfolio analysis
complex_text = """
During fiscal year 2023, the investment portfolio experienced significant setbacks.
Real estate holdings depreciated by $1.2 million due to declining property values.
The equity portfolio lost $800,000 from technology sector exposure.
Bond holdings decreased in value by $300,000 amid rising interest rates.
Total portfolio losses amounted to $2.3 million, representing a 15% decline.
"""

result = lx.extract(
    text_or_documents=complex_text,
    prompt_description=prompt_description,
    examples=examples,
    model_id="gemini-2.5-flash",
)

# The extraction will identify multiple loss events, amounts, and causes
# organized by asset class and time period
```

## Key Features for Financial Extraction

1. **Precise Amount Grounding**: Maps each financial loss to its exact mention in the text
2. **Structured Attributes**: Captures metadata like currency, time periods, and loss categories
3. **Contextual Understanding**: Distinguishes between different types of losses and their causes
4. **Entity Relationships**: Links loss amounts to affected entities and time periods

## Use Cases

This extraction pattern is valuable for:
- **Financial Analysis**: Automatically extract loss data from financial reports
- **Risk Assessment**: Identify patterns in financial losses across documents
- **Compliance**: Track and document financial losses for regulatory purposes
- **Research**: Analyze historical financial loss patterns from news and reports

---

**Note**: This example demonstrates LangExtract's capability to structure financial narratives. For production use in financial contexts, ensure compliance with relevant regulations and combine automated extraction with human review for critical decisions.
