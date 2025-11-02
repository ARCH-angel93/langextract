# Financial Loss Extraction Example

This example demonstrates using LangExtract to extract structured information about financial losses ("lost wealth") from text documents.

## Overview

The example shows how to:
- Extract loss amounts, entities, causes, and time periods
- Structure financial narrative data automatically
- Visualize extracted financial information

## Files

- `demo_financial_loss.py` - Main demo script showing the extraction

## Running the Example

### Prerequisites

1. Install LangExtract:
   ```bash
   pip install langextract
   ```

2. Set up your API key (choose one method):
   ```bash
   # Option 1: Environment variable
   export LANGEXTRACT_API_KEY="your-api-key-here"
   
   # Option 2: .env file
   echo 'LANGEXTRACT_API_KEY=your-api-key-here' >> .env
   ```

### Run the Demo

```bash
python demo_financial_loss.py
```

## What It Does

The script will:
1. Extract financial loss information from sample text
2. Identify loss amounts, affected entities, causes, and time periods
3. Save results to `financial_losses.jsonl`
4. Generate an interactive HTML visualization

## Example Output

From the text:
> "John Smith lost $50,000 in the stock market crash of 2024."

The extraction identifies:
- **Affected Entity**: "John Smith" (type: individual)
- **Loss Amount**: "$50,000" (currency: USD)
- **Loss Event**: "stock market crash of 2024" (type: market_event)
- **Time Period**: "2024" (year: 2024)

## Use Cases

This pattern is useful for:
- Financial report analysis
- Investment loss tracking
- Risk assessment and auditing
- Historical financial analysis

## Documentation

For more details, see:
- [Full Financial Loss Example Documentation](../../docs/examples/financial_loss_example.md)
- [LangExtract Main README](../../README.md)

---

*Disclaimer: This is for demonstration purposes only and does not constitute financial advice.*
